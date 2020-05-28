<template>
    <div>
    <h3>整体报告</h3>
    <el-row>
    <el-col :span="12" :offset="6">
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="algo"
        label="算法"
        width="180">
      </el-table-column>
      <el-table-column
        prop="precision"
        label="Precision"
        width="180">
      </el-table-column>
      <el-table-column
        prop="recall"
        label="Recall"
        width="180">
      </el-table-column>
      <el-table-column
        prop="f1score"
        label="F1-score"
        width="180">
      </el-table-column>
    </el-table>
    </el-col>
    </el-row>
    </div>
</template>

<script>
export default {
  mounted () {
    this.getReport()
  },
  methods: {
    async getReport () {
      let tmp = await this.$axios
        .get('http://localhost:8081/report', {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function (error) { // 请求失败处理
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
    }
  },
  data () {
    return {
      report: {},
      tableData: []
    }
  }
}
</script>
