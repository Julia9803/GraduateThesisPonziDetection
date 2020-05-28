<template>
    <div>
        <h3>整体展示图</h3>
        <el-row>
            <el-col :span="11" :offset="7">
                <div id="chart" :style="{width: '600px', height: '500px'}"></div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  mounted () {
    this.getChartData()
  },
  methods: {
    async getChartData () {
      let res = await this.$axios
        .get('http://localhost:8081/chartReport', {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
      this.featureImportance = res.data.featureImportance.split('&')
      this.featureName = res.data.featureName.split('&')
      console.log(this.featureImportance)
      console.log(this.featureName)
      this.pic()
    },
    pic () {
      let chart = this.$echarts.init(document.getElementById('chart'))
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
