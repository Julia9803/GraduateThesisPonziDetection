import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/pages/main'
import Config from '@/pages/config'
import Report from '@/pages/report'
import Search from '@/pages/search'
import Chart from '@/pages/chart'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        {
          path: '/config',
          component: Config
        },
        {
          path: '/report',
          component: Report
        },
        {
          path: '/search',
          component: Search
        },
        {
          path: '/chart',
          component: Chart
        }
      ]
    }
  ]
})
