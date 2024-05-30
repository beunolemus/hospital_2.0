import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginVuew from '@/components/login.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginVuew
    },
   {
      path: '/register',
      name: 'register',
      component: RegisterUser
    }

  ]
})

export default router
