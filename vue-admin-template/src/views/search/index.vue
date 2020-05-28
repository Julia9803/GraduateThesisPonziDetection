<template>
  <div class="app-container">
    <h3>查询单个合约</h3>
    <el-row>
      <el-col :span="8" :offset="6">
        <el-input v-model="address" placeholder="请输入查询地址" @keyup.native="keyup()" />
      </el-col>
      <el-col :span="4">
        <el-button type="primary" icon="el-icon-search" @click="search">查询</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8" :offset="6">
        <el-card v-show="show" class="box-card" align="center">
          <div v-if="ponzi">
            <h3>{{ address }}是庞氏合约</h3>
          </div>
          <div v-else>
            <h3>{{ address }}不是庞氏合约</h3>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      address: '',
      ponzi: 'false',
      show: 'true'
    }
  },
  mounted() {
    this.show = false
  },
  methods: {
    search() {
      this.getSingleReport(this.address)
    },
    getSingleReport() {
      this.$axios
        .get(`http://localhost:8081/singleReport?address=${this.address}`, {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .then(response => (
          this.ponzi = response.data))
        .catch(function(error) { // 请求失败处理
          console.log(error)
        })
      this.modal()
      this.show = true
      console.log(this.ponzi)
    },
    modal() {
      this.$notify({
        title: '成功',
        message: '查询成功',
        type: 'success'
      })
    },
    keyup() {
      if (this.address.length < 42) {
        this.show = false
      }
    }
  }
}
</script>

<style>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 10px;
  }

  .box-card {
    margin-top: 20px;
    width: 480px;
  }
</style>

