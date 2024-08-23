<template>
  <section class="bg-gray-100 min-h-screen flex justify-center items-center">
    <div class="bg-gray-300 rounded-2xl p-10 flex flex-col items-center max-w-2xl w-full">
      <div class="w-full px-8">
        <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Registro de Cirugía</h2>
        <p class="text-sm mb-8 text-[#002D74]">Bienvenido al registro de Cirugía</p>
        
        <form @submit.prevent="registerSurgery" class="flex flex-col gap-4">
          <!-- Sección de Datos de la Cirugía -->
          <div class="flex flex-wrap gap-4">
            <h3 class="font-bold text-xl text-[#0F6466] w-full mb-2">Detalles de la Cirugía</h3>
          <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="number" v-model="paciente_id" placeholder="Paciente_ID" required>
              <select class="p-2 mt-2 rounded-xl border flex-1" v-model="espacio_medico_id" required>
                <option value="" disabled>Espacio_Medico_ID</option>
                <option value="1">Quirófano	A-106</option>
                <option value="2">Quirófano	A-107</option>
                <option value="3">Quirófano  A-108</option>
              </select>
          </div>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="nombre" placeholder="Nombre de la Cirugía" required>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="descripcion" placeholder="Descripción" required>
          </div>
          <div class="flex flex-wrap gap-4">
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="tipo" placeholder="Tipo" required>
            <select class="p-2 mt-2 rounded-xl border flex-1" v-model="nivelUrgencia" required>
              <option value="" disabled>Nivel de Urgencia</option>
              <option value="Bajo">Bajo</option>
              <option value="Medio">Medio</option>
              <option value="Alto">Alto</option>
            </select>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="datetime-local" v-model="horario" placeholder="Horario" required>
          </div>
          <div class="flex flex-wrap gap-4">
            <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="observaciones" placeholder="Observaciones"></textarea>
            <textarea class="p-2 mt-2 rounded-xl border flex-1" v-model="valoracionMedica" placeholder="Valoración Médica"></textarea>
          </div>
          <div class="flex flex-wrap gap-4">
            <select class="p-2 mt-2 rounded-xl border flex-1" v-model="estatus" required>
              <option value="" disabled>Estatus</option>
              <option value="Programada">Programada</option>
              <option value="EnCurso">En Curso</option>
              <option value="Completada">Completada</option>
              <option value="Cancelada">Cancelada</option>
            </select>
            <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="consumible" placeholder="Consumible" required>
          </div>
          <RouterLink to="/tablaC">
          <div class="w-full">
            <button class="bg-gray-500 text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Registrar</button>
          </div>
        </RouterLink>
          <div class="w-full">
            <button class="bg-gray-500 text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="button" @click="goToSurgeryList">Lista de Cirugías</button>
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
  methods: {
    async registerSurgery() {
      const fechaActual = new Date().toISOString();
      const nuevaCirugia = {
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
        Fecha_Registro: fechaActual,
        Fecha_Actualizacion: fechaActual
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/cirugias/', nuevaCirugia);
        console.log("Cirugía registrada:", response.data);
        // Limpia los campos después de registrar la cirugía
        this.paciente_id = '',
        this.espacio_medico_id = '',
        this.tipo = '';
        this.nombre = '';
        this.descripcion = '';
        this.nivelUrgencia = '';
        this.horario = '';
        this.observaciones = '';
        this.valoracionMedica = '';
        this.estatus = '';
        this.consumible = '';
      } catch (error) {
        console.error("Error al registrar la cirugía:", error);
      }
    },
    goToSurgeryList() {
      this.$router.push('/tablaC');
    }
  }
};
</script>
