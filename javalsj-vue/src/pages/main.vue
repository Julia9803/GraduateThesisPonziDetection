<template>
    <div>
        <el-row class="tac">
  <el-col :span="6">
    <h5>导航栏</h5>
    <el-menu
      default-active="$route.path"
      class="el-menu-vertical-demo"
      router=""
      @open="handleOpen"
      @close="handleClose">
      <el-menu-item index="/report">
          <i class="el-icon-location"></i>
          <span>整体报告</span>
      </el-menu-item>
      <el-menu-item index="/search">
        <i class="el-icon-document"></i>
        <span slot="title">查询单体报告</span>
      </el-menu-item>
      <el-menu-item index="/chart">
        <i class="el-icon-menu"></i>
        <span slot="title">整体展示图</span>
      </el-menu-item>
      <el-menu-item index="/config">
        <i class="el-icon-setting"></i>
        <span slot="title">配置模型</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  <el-col :span="18">
    <el-container>
            <el-header>
                <h1>{{msg}}</h1>
            </el-header>
            <el-main>
              <router-view/>
            </el-main>
        </el-container>
  </el-col>
</el-row>
    </div>
</template>

<script>
import report from './report'
export default {
  data () {
    return {
      msg: 'Welcome to TBAS Ponzi Detector!'
    }
  },
  components: {
    report
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>
