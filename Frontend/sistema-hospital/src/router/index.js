import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginVuew from '@/components/login.vue'
import dashboard from '@/components/dashboard.vue'
import Persona from '@/components/persona.vue'
import Calendar from '@/components/calendar.vue'


import RegisterC from '@/components/RegisterC.vue'



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
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard,
      children:[
        {path:'/persona',name:'persona', component : Persona},
<<<<<<< HEAD
        {path:'/calendario',name:'calendar', component : Calendar}
=======

        {path:"/registerC",name:"registerC",component:RegisterC}
>>>>>>> master
      ]
    }
  ]
})

export default router


