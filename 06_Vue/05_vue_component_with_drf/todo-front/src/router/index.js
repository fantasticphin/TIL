import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

// Vuerouter를 사용하기 위한 코드
Vue.use(VueRouter)

//router와 components를 연결()
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  }
]

const router = new VueRouter({
  // vue-router 설치할 때 설정했던 History 모드
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
