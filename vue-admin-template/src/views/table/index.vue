<template>
  <div class="app-container">
    <h3>
      交易数据样本展示
    </h3>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="Txhash" width="300">
        <template slot-scope="scope">
          {{ scope.row.txhash }}
        </template>
      </el-table-column>
      <el-table-column label="FromAddress">
        <template slot-scope="scope">
          {{ scope.row.fromAddress }}
        </template>
      </el-table-column>
      <el-table-column label="ToAddress" width="350" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.toAddress }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Value" width="200" align="center">
        <template slot-scope="scope">
          {{ scope.row.value }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Class" width="100" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.Class | statusFilter">{{ scope.row.Class }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Age" width="120">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.age }}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'

export default {
  filters: {
    statusFilter(Class) {
      const statusMap = {
        ponzi: 'danger',
        non_ponzi: 'success'
      }
      return statusMap[Class]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        this.listLoading = false
      })
    }
  }
}
</script>
