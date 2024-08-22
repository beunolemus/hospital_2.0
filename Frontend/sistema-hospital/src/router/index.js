import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginVuew from '@/components/login.vue'
import dashboard from '@/components/dashboard.vue'
import Persona from '@/components/persona.vue'
<<<<<<< HEAD
// seccion de cirugias
import Calendar from '@/components/calendar.vue'
import RegisterC from '@/components/RegisterC.vue'
import tablaC from '@/components/tablaC.vue'
import GraficasC from '@/components/graficasC.vue'
import CrearC from '@/components/CrearC.vue'
=======
import Calendar from '@/components/calendar.vue'
import horarios from '@/components/horarios.vue'


import RegisterC from '@/components/RegisterC.vue'

import tablaC from '@/components/tablaC.vue'

import EditCirugia  from '@/components/EditCirugia.vue'

import GraficasC from '@/components/graficasC.vue'
import CrearC from '@/components/CrearC.vue'
import Listahorarios from '@/components/listahorarios.vue'
import Edithorario from '@/components/Edithorario.vue'
>>>>>>> Diego


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

        {path:'/calendario',name:'calendar', component : Calendar},

        {path:"/registerC",name:"registerC",component:RegisterC},

=======
>>>>>>> Diego
        {path:'/calendario',name:'calendar', component : Calendar},

        {path:"/registerC",name:"registerC",component:RegisterC},

        {path:"/tablac",name:"tablac",component:tablaC},

<<<<<<< HEAD
=======
        {path:"/EditCirugia",name:"EditCirugia",component:EditCirugia},

        {path:"/horarios",name:"horarios",component:horarios},

        {path:"/listahorarios",name:"listahorarios",component:Listahorarios},

        {path:"/edithorario",name:"edithorario",component:Edithorario},
        
>>>>>>> Diego
        {path:"/graficasC",name:"graficasC",component:GraficasC},

        {path:"/crearC",name:"crearC",component:CrearC}

       
<<<<<<< HEAD

=======
>>>>>>> Diego
      ]
    }
  ]
})

export default router


