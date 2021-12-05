import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: MainPage,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue')
      },
      {
        path: '/users',
        name: 'users',
        component: () => import('@/views/Users.vue')
      },
      {
        path: '/simulador',
        name: 'simulador',
        component: () => import('@/views/Simulador.vue')
      },
      {
        path: '/dados-coletados',
        name: 'dados-coletados',
        component: () => import('@/views/DadosColetados.vue')
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
