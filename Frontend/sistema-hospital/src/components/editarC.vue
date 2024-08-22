<template>
  <section class="bg-gray-100 min-h-screen flex justify-center items-center">
    <div class="bg-gray-300 rounded-2xl p-10 flex flex-col items-center max-w-2xl w-full relative">
      <!-- Botón de Cierre -->
      <button @click="closeForm" class="absolute top-4 right-4 text-xl font-bold text-gray-600 hover:text-gray-900">
        X
      </button>
      
      <div class="w-full px-8">
        <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Editar Cirugía</h2>
        <p class="text-sm mb-8 text-[#002D74]">Modifique los detalles de la cirugía</p>

        <form @submit.prevent="updateSurgery" class="flex flex-col gap-4">
          <!-- Sección de Datos de la Cirugía -->
          <div class="flex flex-wrap gap-4">
            <h3 class="font-bold text-xl text-[#0F6466] w-full mb-2">Detalles de la Cirugía</h3>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="number" v-model="paciente_id" placeholder="Paciente_ID" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="number" v-model="espacio_medico_id" placeholder="Espacio_Medico_ID" required>
          </div>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="nombre" placeholder="Nombre de la Cirugía">
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="descripcion" placeholder="Descripción">
          </div>
          <div class="flex flex-wrap gap-4">
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="tipo" placeholder="Tipo">
            <select class="p-2 mt-2 rounded-xl border flex-1" v-model="nivelUrgencia">
              <option value="" disabled>Nivel de Urgencia</option>
              <option value="Bajo">Bajo</option>
              <option value="Medio">Medio</option>
              <option value="Alto">Alto</option>
            </select>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="datetime-local" v-model="horario" placeholder="Horario">
          </div>
          <div class="flex flex-wrap gap-4">
            <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="observaciones" placeholder="Observaciones"></textarea>
            <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="valoracionMedica" placeholder="Valoración Médica"></textarea>
          </div>
          <div class="flex flex-wrap gap-4">
            <select class="p-2 mt-2 rounded-xl border flex-1" v-model="estatus">
              <option value="" disabled>Estatus</option>
              <option value="Programada">Programada</option>
              <option value="EnCurso">En Curso</option>
              <option value="Completada">Completada</option>
              <option value="Cancelada">Cancelada</option>
            </select>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="consumible" placeholder="Consumible">
          </div>
          <div class="w-full">
            <button class="bg-gray-500 text-white py-2 rounded-xl w-full hover:scale-105 duration-300" type="submit">Actualizar</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
data() {
  return {
    paciente_id:'',
    espacio_medico_id:'',
    tipo: '',
    nombre: '',
    descripcion: '',
    nivelUrgencia: '',
    horario: '',
    observaciones: '',
    valoracionMedica: '',
    estatus: '',
    consumible: ''
  };
},
created() {
  this.cargarDatosCirugia();
},
methods: {
  async cargarDatosCirugia() {
    const id = this.$route.params.id;
    const token = localStorage.getItem('token'); // Verifica que esta clave sea correcta
    try {
      const response = await axios.get(`http://127.0.0.1:8000/cirugia/${id}/`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      const cirugia = response.data;
      this.paciente_id = cirugia.Paciente_ID || '';
      this.espacio_medico_id = cirugia.Espacio_Medico_ID || '';
      this.tipo = cirugia.Tipo || '';
      this.nombre = cirugia.Nombre || '';
      this.descripcion = cirugia.Descripcion || '';
      this.nivelUrgencia = cirugia.Nivel_Urgencia || '';
      this.horario = cirugia.Horario || '';
      this.observaciones = cirugia.Observaciones || '';
      this.valoracionMedica = cirugia.Valoracion_Medica || '';
      this.estatus = cirugia.Estatus || '';
      this.consumible = cirugia.Consumible || '';
    } catch (error) {
      console.error("Error al cargar los datos de la cirugía:", error.response ? error.response.data : error.message);
    }
  },

  async updateSurgery() {
    const id = this.$route.params.id;
    const fechaActual = new Date().toISOString();
    const cirugiaActualizada = {
      Paciente_ID: this.paciente_id,
      Espacio_Medico_ID: this.espacio_medico_id,
      Tipo: this.tipo,
      Nombre: this.nombre,
      Descripcion: this.descripcion,
      Nivel_Urgencia: this.nivelUrgencia,
      Horario: this.horario,
      Observaciones: this.observaciones,
      Valoracion_Medica: this.valoracionMedica,
      Estatus: this.estatus,
      Consumible: this.consumible,
      Fecha_Actualizacion: fechaActual
    };

    const token = localStorage.getItem('token'); // Verifica que esta clave sea correcta

    try {
      const response = await axios.put(`http://127.0.0.1:8000/cirugia/${id}/`, cirugiaActualizada, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      console.log("Cirugía actualizada correctamente", response);
      this.$router.push('/tablaC'); // Redirecciona a la lista de cirugías después de la actualización
    } catch (error) {
      console.error("Error al actualizar la cirugía:", error.response ? error.response.data : error.message);
      // Aquí podrías mostrar un mensaje de error al usuario
    }
  },

  closeForm() {
    this.$router.push('/tablaC'); // Redirecciona a la lista de cirugías o a otra vista según sea necesario
  }
}
}
</script>

<style scoped>
button {
background: none;
border: none;
cursor: pointer;
font-size: 1.5rem;
color: #333;
}
button:hover {
color: #000;
}
</style>
