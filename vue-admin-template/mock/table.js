// import Mock from 'mockjs'
import transactions from '../src/assets/json_data/trans_frontend_show.json'
import transactions1 from '../src/assets/json_data/trans_frontend_show1.json'
import transactions2 from '../src/assets/json_data/trans_frontend_show2.json'

// const data = Mock.mock({
//   'items|30': [{
//     id: '@id',
//     title: '@sentence(10, 20)',
//     'status|1': ['published', 'draft', 'deleted'],
//     author: 'name',
//     display_time: '@datetime',
//     pageviews: '@integer(300, 5000)'
//   }]
// })
const data = transactions
const dataA = transactions1
const dataB = transactions2

export default [
  {
    url: '/vue-admin-template/table/list',
    type: 'get',
    response: config => {
      // const items = data.items
      return {
        code: 20000,
        data: {
          total: 100,
          items: data
        }
      }
    }
  },
  {
    url: '/vue-admin-template/table/a',
    type: 'get',
    response: config => {
      // const items = data.items
      return {
        code: 20000,
        data: {
          total: 100,
          items: dataA
        }
      }
    }
  },
  {
    url: '/vue-admin-template/table/b',
    type: 'get',
    response: config => {
      // const items = data.items
      return {
        code: 20000,
        data: {
          total: 100,
          items: dataB
        }
      }
    }
  }

]
