<template>
    <div>
        <h3>查询单体报告</h3>
        <el-row>
            <el-col :span="8" :offset="6">
                    <el-input v-model="address" placeholder="请输入查询地址"></el-input>
                </el-col>
                <el-col :span="4">
                    <el-button type="primary" icon="el-icon-search" v-on:click="search">查询</el-button>
            </el-col>
            </el-row>
            <div v-show="show">
                    <div v-if="ponzi">
                        <h3>{{address}}是旁氏合约</h3>
                    </div>
                    <div v-else>
                        <h3>{{address}}不是旁氏合约</h3>
                    </div>
            </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      address: '',
      ponzi: 'false',
      show: 'true'
    }
  },
  mounted () {
    this.show = false
  },
  methods: {
    search () {
      this.getSingleReport(this.address)
    },
    getSingleReport () {
      this.$axios
        .get(`http://localhost:8081/singleReport?address=${this.address}`, {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .then(response => (
          this.ponzi = response.data))
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
      this.show = true
      console.log(this.ponzi)
    }
  }
}
</script>
