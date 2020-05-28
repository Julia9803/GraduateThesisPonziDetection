<template>
  <div class="dashboard-container">
    <div class="dashboard-text">Welcome: {{ name }}</div>
    <h3>整体检测结果</h3>
    <el-row>
      <el-col :span="12" :offset="6">
        <el-table
          :data="tableData"
          style="width: 100%"
        >
          <el-table-column
            prop="algo"
            label="算法"
            width="180"
          />
          <el-table-column
            prop="precision"
            label="Precision"
            width="180"
          />
          <el-table-column
            prop="recall"
            label="Recall"
            width="180"
          />
          <el-table-column
            prop="f1score"
            label="F1-score"
            width="180"
          />
        </el-table>
      </el-col>
    </el-row>
    <h3>特征重要性展示图</h3>
    <el-row>
      <el-col :span="11" :offset="7">
        <div id="chart" :style="{width: '600px', height: '500px'}" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      report: {},
      tableData: []
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    this.getReport()
    this.getChartData()
  },
  methods: {
    async getReport() {
      const tmp = await this.$axios
        .get('http://localhost:8081/report', {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function(error) { // 请求失败处理
          console.log(error)
        })
      this.report = tmp.data
      this.tableData = [{
        algo: 'Random Forest',
        precision: this.report.rfPrecision,
        recall: this.report.rfRecall,
        f1score: this.report.rfF1Score
      }, {
        algo: 'XGBoost',
        precision: this.report.xgbPrecision,
        recall: this.report.xgbRecall,
        f1score: this.report.xgbF1Score
      }, {
        algo: 'lightGBM',
        precision: this.report.lgbPrecision,
        recall: this.report.lgbRecall,
        f1score: this.report.lgbF1Score
      }]
      console.log(this.tableData)
    },
    async getChartData() {
      const res = await this.$axios
        .get('http://localhost:8081/chartReport', {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function(error) { // 请求失败处理
          console.log(error)
        })
      this.featureImportance = res.data.featureImportance.split('&')
      this.featureName = res.data.featureName.split('&')
      console.log(this.featureImportance)
      console.log(this.featureName)
      this.pic()
    },
    pic() {
      const chart = this.$echarts.init(document.getElementById('chart'))
      chart.setOption({
        title: {
          text: 'Features',
          subtext: 'Top 10'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['Feature importance']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
          boundaryGap: [0, 0.01]
        },
        yAxis: {
          type: 'category',
          data: this.featureName
        },
        series: [
          {
            name: 'Feature importance',
            type: 'bar',
            data: this.featureImportance
          }
        ]
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
