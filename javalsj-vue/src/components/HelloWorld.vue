<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>全体报告</h2>
    <!-- <div v-for="(value,key) in report">
      {{key}} : {{value}}
    </div> -->
    <h2>查询单体报告</h2>
    <input v-model="address">
    <button v-on:click="getSingleReport()">查询</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to TBAS Ponzi Detector!',
      address: ''
    }
  },
  mounted () {
    this.$axios
      .get('https://localhost:8081/report')
      .then(response => (this.report = JSON.parse(response)))
      .catch(function (error) { // 请求失败处理
        console.log(error)
      })
    this.$axios
      .get('https://localhost:8081/chartReport')
      .then(response => (this.chartreport = JSON.parse(response)))
      .catch(function (error) { // 请求失败处理
        console.log(error)
      })
  },
  getSingleReport () {
    this.$axios
      .get('https://localhost:8081/singleReport{address}')
      .then(response => (this.singlereport = JSON.parse(response)))
      .catch(function (error) { // 请求失败处理
        console.log(error)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
