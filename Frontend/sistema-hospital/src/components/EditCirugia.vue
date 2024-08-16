<template>
    <section class="bg-gray-100 min-h-screen flex justify-center items-center">
      <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-2xl w-full">
        <div class="w-full px-8">
          <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Editar Cirugía</h2>
          <p class="text-sm mb-8 text-[#002D74]">Edita los detalles de la cirugía seleccionada</p>
  
          <form @submit.prevent="updateSurgery" class="flex flex-col gap-4">
            <!-- Sección de Datos de la Cirugía -->
            <div class="flex flex-wrap gap-4">
              <h3 class="font-bold text-xl text-[#0F6466] w-full mb-2">Detalles de la Cirugía</h3>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="cirugia.nombreCirugia" placeholder="Nombre de la Cirugía" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="cirugia.descripcion" placeholder="Descripción" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <select class="p-2 mt-2 rounded-xl border flex-1" v-model="cirugia.nivelUrgencia" required>
                <option value="" disabled>Nivel de Urgencia</option>
                <option value="Bajo">Bajo</option>
                <option value="Medio">Medio</option>
                <option value="Alto">Alto</option>
              </select>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="datetime-local" v-model="cirugia.horario" placeholder="Horario" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="cirugia.observaciones" placeholder="Observaciones"></textarea>
              <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="cirugia.valoracionMedica" placeholder="Valoración Médica"></textarea>
            </div>
            <div class="flex flex-wrap gap-4">
              <select class="p-2 mt-2 rounded-xl border flex-1" v-model="cirugia.estatus" required>
                <option value="" disabled>Estatus</option>
                <option value="Programada">Programada</option>
                <option value="EnCurso">En Curso</option>
                <option value="Completada">Completada</option>
                <option value="Cancelada">Cancelada</option>
              </select>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="cirugia.consumible" placeholder="Consumible" required>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Guardar Cambios</button>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="button" @click="goBack">Cancelar</button>
            </div>
          </form>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cirugia: {
          nombreCirugia: '',
          descripcion: '',
          nivelUrgencia: '',
          horario: '',
          observaciones: '',
          valoracionMedica: '',
          estatus: '',
          consumible: ''
        }
      };
    },
    created() {
      // Aquí deberías cargar los datos de la cirugía que deseas editar
      // Esto puede ser a través de una API llamando un método de tu backend
      // Por ejemplo:
      // this.cargarDatosCirugia();
    },
    methods: {
      updateSurgery() {
        // Aquí puedes agregar la lógica para enviar los datos editados al backend
        console.log("Cirugía actualizada:", this.cirugia);
  
        // Redirigir a otra vista después de guardar
        this.goBack();
      },
      goBack() {
        window.location.href = 'http://localhost:5173/EditCirugia'; // Redirige de nuevo a la lista de cirugías
      },    
      cargarDatosCirugia() {
        // Supongamos que recibes el ID de la cirugía por query params
        const idCirugia = this.$route.query.id;
        // Aquí harías una llamada a la API para obtener los datos de la cirugía con el ID
        // Ejemplo: 
        // axios.get(`tu-api/cirugias/${idCirugia}`).then(response => {
        //   this.cirugia = response.data;
        // });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Aquí puedes agregar estilos específicos para tu componente */
  </style>
  