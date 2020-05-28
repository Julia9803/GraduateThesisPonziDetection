import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/vue-admin-template/table/list',
    method: 'get',
    params
  })
}

export function getList1(params) {
  return request({
    url: '/vue-admin-template/table/a',
    method: 'get',
    params
  })
}

export function getList2(params) {
  return request({
    url: '/vue-admin-template/table/b',
    method: 'get',
    params
  })
}
