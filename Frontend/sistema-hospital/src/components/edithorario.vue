<template>
    <section class="bg-gray-100 min-h-screen flex justify-center items-center">
      <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-2xl w-full">
        <div class="w-full px-8">
          <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Editar Horario</h2>
          <p class="text-sm mb-8 text-[#002D74]">Actualiza los detalles del horario existente</p>
  
          <form @submit.prevent="editarHorario" class="flex flex-col gap-4">
            <!-- Sección de Datos del Horario -->
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="number" v-model="horario.empleado_id" placeholder="ID del Empleado" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.nombre" placeholder="Nombre del Horario" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.especialidad" placeholder="Especialidad" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.dia_semana" placeholder="Día de la Semana" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="time" v-model="horario.hora_inicio" placeholder="Hora de Inicio" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="time" v-model="horario.hora_fin" placeholder="Hora de Fin" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.turno" placeholder="Turno" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.nombre_departamento" placeholder="Nombre del Departamento" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="horario.nombre_sala" placeholder="Nombre de la Sala" required>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Guardar Cambios</button>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="button" @click="goBack">Cancelar</button>
            </div>
          </form>
          
          <!-- Botón para volver a la lista de horarios -->
          <div class="w-full mt-4">
            <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" @click="goToList">Ver Lista de Horarios</button>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        horario: {
          empleado_id: '',
          nombre: '',
          especialidad: '',
          dia_semana: '',
          hora_inicio: '',
          hora_fin: '',
          turno: '',
          nombre_departamento: '',
          nombre_sala: ''
        }
      };
    },
    methods: {
      editarHorario() {
        // Lógica para enviar los datos actualizados al backend
        console.log("Horario actualizado:", this.horario);
        this.goBack(); // Redirigir después de guardar
      },
      goBack() {
        window.location.href = 'http://localhost:5173/horarios'; // Redirige a la lista de horarios
      },
      goToList() {
        window.location.href = 'http://localhost:5173/listahorarios'; // Redirige a la lista de horarios
      }
    },
    async mounted() {
      const horarioId = this.$route.params.id;
      // Aquí cargarías los datos del horario desde tu backend
      // Por simplicidad, asumiremos que ya tienes los datos cargados en `this.horario`
    }
  };
  </script>
  
  <style scoped>
  /* Estilos personalizados para el componente */
  </style>
  