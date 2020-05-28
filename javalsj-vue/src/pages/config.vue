<template>
    <div>
        <el-row>
        <el-col :offset="2" :span="18">
        <div style="text-align: left">
        <el-steps :active="active" finish-status="success">
            <el-step title="配置数据"></el-step>
            <el-step title="配置特征"></el-step>
            <el-step title="配置模型"></el-step>
            <el-step title="生成报告"></el-step>
        </el-steps>
        </div>

        <div style="margin-top: 12px;" class="data" v-if="active === 0">
            <el-select v-model="data" placeholder="请选择">
                <el-option
                    v-for="item in config_data"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div style="margin-top: 12px;" class="feature" v-if="active === 1">
            <el-select v-model="feature" placeholder="请选择">
                <el-option
                    v-for="item in config_feature"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-input-number v-model="N_num" :min="1" :max="11" label="N-Gram中N的值"></el-input-number>
        </div>
        <div style="margin-top: 12px;" class="model" v-if="active === 2">
            <el-select v-model="model" placeholder="请选择">
                <el-option
                    v-for="item in config_model"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div style="margin-top: 12px;" class="report" v-if="active === 4">
            <h3>整体报告</h3>
            <el-row v-show="show">
                <el-col :span="20" :offset="2">
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

        <el-button style="margin-top: 24px;" @click="back">上一步</el-button>
        <el-button style="margin-top: 24px;" @click="next">下一步</el-button>
        </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  data () {
    return {
      active: 0,
      config: [],
      config_data: [{
        value: '选项1',
        label: '数据集1'
      }, {
        value: '选项2',
        label: '数据集2'
      }],
      config_feature: [{
        value: 'ALL',
        label: 'ALL'
      }, {
        value: 'APF',
        label: 'APF'
      }, {
        value: 'TBF',
        label: 'TBF'
      }],
      config_model: [{
        value: 'RF',
        label: 'Random Forest'
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
      N_num: 1
    }
  },
  methods: {
    next () {
      if (this.active < 4) {
        this.active++
        if (this.active === 4) {
          this.getConfig()
          this.show = true
        }
      }
    },
    back () {
      if (this.active > 0) this.active--
    },
    async getConfig () {
      this.modal()
      let res = await this.$axios
        .get(`http://localhost:8000/config?method=${this.feature}&N=${this.N_num}&model=${this.model}`, {
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }})
        .catch(function (error) { // 请求失败处理
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
    modal () {
      this.$notify({
        title: '成功',
        message: '系统配置成功',
        type: 'success'
      })
    }
  }
}
</script>
