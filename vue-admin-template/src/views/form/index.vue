<template>
  <div class="app-container">
    <h3>
      个性化模型配置
    </h3>
    <el-row>
      <el-col :offset="2" :span="18">
        <div style="text-align: left">
          <el-steps :active="active" finish-status="success">
            <el-step title="配置数据" />
            <el-step title="配置特征" />
            <el-step title="配置模型" />
            <el-step title="生成报告" />
          </el-steps>
        </div>
        <div v-if="active === 0" style="margin-top: 30px;" class="data">
          <el-select v-model="data" placeholder="请选择数据">
            <el-option
              v-for="item in config_data"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
        <div v-if="active === 1" style="margin-top: 30px;" class="feature">
          <el-select v-model="feature" placeholder="请选择特征">
            <el-option
              v-for="item in config_feature"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
          <el-select v-model="N_num" placeholder="请选择N-Gram中N的值">
            <el-option
              v-for="item in config_N"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
        <div v-if="active === 2" style="margin-top: 30px;" class="model">
          <el-select v-model="model" placeholder="请选择模型">
            <el-option
              v-for="item in config_model"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
        <div v-if="active === 4" style="margin-top: 30px;" class="report">
          <h3>整体报告</h3>
          <el-row v-show="show">
            <el-col :span="20" :offset="2">
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
          </el-row>       </div>
        <div v-show="data === config_data[0].value" style="margin-top: 30px;" class="table1">
          <el-table
            v-loading="listLoading1"
            :data="list1"
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
        <div v-show="data === config_data[1].value" style="margin-top: 30px;" class="table2">
          <el-table
            v-loading="listLoading2"
            :data="list2"
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
        <el-button style="margin-top: 24px;" @click="back">上一步</el-button>
        <el-button style="margin-top: 24px;" @click="next">下一步</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getList1, getList2 } from '@/api/table'

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
      list1: null,
      list2: null,
      listLoading1: true,
      listLoading2: true,
      active: 0,
      config: [],
      config_data: [{
        value: '选项1',
        label: '随机数据集1'
      }, {
        value: '选项2',
        label: '随机数据集2'
      }],
      config_feature: [{
        value: 'ALL',
        label: 'ALL(所有特征)'
      }, {
        value: 'APF',
        label: 'APF(账户对特征)'
      }, {
        value: 'TBF',
        label: 'TBF(交易行为特征)'
      }],
      config_N: [{
        value: 1,
        label: '1'
      }, {
        value: 2,
        label: '2'
      }, {
        value: 3,
        label: '3'
      }, {
        value: 4,
        label: '4'
      }, {
        value: 5,
        label: '5'
      }, {
        value: 6,
        label: '6'
      }, {
        value: 7,
        label: '7'
      }, {
        value: 8,
        label: '8'
      }, {
        value: 9,
        label: '9'
      }, {
        value: 10,
        label: '10'
      }, {
        value: 11,
        label: '1-10'
      }],
      config_model: [{
        value: 'RF',
        label: 'Random Forest(随机森林)'
      }, {
        value: 'XGBoost',
        label: 'XGBoost'
      }, {
        value: 'LightGBM',
        label: 'LightGBM'
      }],
      tableData: {},
      data: '',
      feature: '',
      model: '',
      show: false,
      N_num: null
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading1 = true
      getList1().then(response => {
        this.list1 = response.data.items
        this.listLoading1 = false
      })
      this.listLoading2 = true
      getList2().then(response => {
        this.list2 = response.data.items
        this.listLoading2 = false
      })
    },
    next() {
      this.data = null
      if (this.active < 4) {
        this.active++
        if (this.active === 4) {
          this.getConfig()
          this.show = true
        }
      }
    },
    back() {
      if (this.active > 0) this.active--
    },
    async getConfig() {
      this.modal()
      const res = await this.$axios
        .get(`http://localhost:8000/config?method=${this.feature}&N=${this.N_num}&model=${this.model}`, {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function(error) { // 请求失败处理
          console.log(error)
        })
      this.config = res.data
      this.tableData = [{
        algo: this.model,
        precision: this.config.precision,
        recall: this.config.recall,
        f1score: this.config['f1-score']
      }]

      console.log(this.tableData)
    },
    modal() {
      this.$notify({
        title: '成功',
        message: '系统配置成功',
        type: 'success'
      })
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

