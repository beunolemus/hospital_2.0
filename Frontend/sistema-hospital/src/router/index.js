import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginVuew from '@/components/login.vue'
import dashboard from '@/components/dashboard.vue'
import Persona from '@/components/persona.vue'

import horarios from '@/components/horarios.vue'


// cirugias
import Registros from '@/components/AgendaC.vue'
import tablaC from '@/components/tablaC.vue'
import EditCirugia  from '@/components/editarC.vue'
import GraficasC from '@/components/graficasC.vue'
import CrearC from '@/components/CrearC.vue'
//horarios
import Listahorarios from '@/components/listahorarios.vue'
import Edithorario from '@/components/edithorario.vue'


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

        {path:'/registros',name:'registros', component : Registros},

        {path:"/tablac",name:"tablac",component:tablaC},

        {path:"/editarC/:id",name:"EditCirugia",component:EditCirugia},

        {path:"/horarios",name:"horarios",component:horarios},

        {path:"/listahorarios",name:"listahorarios",component:Listahorarios},

        {path:"/edithorario",name:"edithorario",component:Edithorario},
        
        {path:"/graficasC",name:"graficasC",component:GraficasC},

        {path:"/crearC",name:"crearC",component:CrearC}

       
      ]
    }
  ]
})

export default router


