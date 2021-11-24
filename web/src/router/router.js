import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue')
      },
      {
        path: '/register-user',
        name: 'registerUser',
        component: () => import('@/views/RegisterUser.vue')
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
