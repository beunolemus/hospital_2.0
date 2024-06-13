<template>
    <section class="bg-gray-100 min-h-screen flex justify-center items-center">
      <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-2xl w-full">
        <div class="w-full px-8">
          <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Registro de Cirugía</h2>
          <p class="text-sm mb-8 text-[#002D74]">Bienvenido al registro de Cirugía</p>
  
          <form @submit.prevent="registerSurgery" class="flex flex-col gap-4">
            <!-- Sección de Datos del Paciente -->
            <div class="flex flex-wrap gap-4">
              <h3 class="font-bold text-xl text-[#0F6466] w-full mb-2">Datos del Paciente</h3>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="nombrePaciente" placeholder="Nombre del Paciente" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="apellidoPaciente" placeholder="Apellido del Paciente" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="curpPaciente" placeholder="CURP del Paciente" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="tipoSangrePaciente" placeholder="Tipo de Sangre del Paciente" required>
              <select class="p-2 mt-2 rounded-xl border flex-1" v-model="generoPaciente" required>
                <option value="" disabled>Género</option>
                <option value="masculino">Masculino</option>
                <option value="femenino">Femenino</option>
                <option value="otro">Otro</option>
              </select>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="date" v-model="fechaNacimientoPaciente" placeholder="Fecha de Nacimiento" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="tel" v-model="telefonoPaciente" placeholder="Teléfono" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="email" v-model="correoPaciente" placeholder="Correo" required>
            </div>
  
            <!-- Sección de Detalles de la Cirugía -->
            <div class="flex flex-wrap gap-4">
              <h3 class="font-bold text-xl text-[#0F6466] w-full mb-2">Detalles de la Cirugía</h3>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="cirujano" placeholder="Nombre del Cirujano" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="tipoCirugia" placeholder="Tipo de Cirugía" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="date" v-model="fechaCirugia" placeholder="Fecha de Cirugía" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="time" v-model="horaCirugia" placeholder="Hora de Cirugía" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="duracion" placeholder="Duración Estimada (horas)" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="sala" placeholder="Sala de Cirugía" required>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Registrar</button>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="button" @click="goToSurgeryList">Listas de Cirugías</button>
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
        nombrePaciente: '',
        apellidoPaciente: '',
        curpPaciente: '',
        tipoSangrePaciente: '',
        generoPaciente: '',
        fechaNacimientoPaciente: '',
        telefonoPaciente: '',
        correoPaciente: '',
        cirujano: '',
        tipoCirugia: '',
        fechaCirugia: '',
        horaCirugia: '',
        duracion: '',
        sala: ''
      };
    },
    methods: {
      registerSurgery() {
        const nuevaCirugia = {
          nombrePaciente: this.nombrePaciente,
          apellidoPaciente: this.apellidoPaciente,
          curpPaciente: this.curpPaciente,
          tipoSangrePaciente: this.tipoSangrePaciente,
          generoPaciente: this.generoPaciente,
          fechaNacimientoPaciente: this.fechaNacimientoPaciente,
          telefonoPaciente: this.telefonoPaciente,
          correoPaciente: this.correoPaciente,
          cirujano: this.cirujano,
          tipoCirugia: this.tipoCirugia,
          fechaCirugia: this.fechaCirugia,
          horaCirugia: this.horaCirugia,
          duracion: this.duracion,
          sala: this.sala
        };
  
        console.log("Cirugía registrada:", nuevaCirugia);
  
        // Aquí puedes agregar la lógica para enviar los datos al backend
      },
      goToSurgeryList() {
        // Lógica para redirigir a la página de lista de cirugías
        console.log("Redirigiendo a la lista de cirugías...");
      }
    }
  };
  </script>
  
  <style scoped>
  /* Aquí puedes agregar estilos específicos para tu componente */
  </style>
  