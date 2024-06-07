<template>
    <section class="bg-gray-100 min-h-screen flex justify-center items-center">
      <div class="bg-[#D2E8E3] rounded-2xl p-5 flex flex-col items-center max-w-md w-full">
        <div class="w-full px-8">
          <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Registro </h2>
          <p class="text-sm mb-8 text-[#002D74]">Bienvenido al registro de Persona</p>
  
          <form @submit.prevent="register" class="flex flex-col gap-4">
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="nombre" placeholder="Nombre" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="primerApellido" placeholder="Primer Apellido" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="segundoApellido" placeholder="Segundo Apellido" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="curp" placeholder="CURP" required>
              <select class="p-2 mt-2 rounded-xl border flex-1" v-model="genero" required>
                <option value="" disabled>Género</option>
                <option value="masculino">Masculino</option>
                <option value="femenino">Femenino</option>
                <option value="otro">Otro</option>
              </select>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="text" v-model="tipoSangre" placeholder="Tipo de Sangre" required>
            </div>
            <div class="flex flex-wrap gap-4">
              <input class="p-2 mt-2 rounded-xl border flex-1" type="date" v-model="fechaNacimiento" placeholder="Fecha de Nacimiento" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="tel" v-model="telefono" placeholder="Teléfono" required>
              <input class="p-2 mt-2 rounded-xl border flex-1" type="email" v-model="correo" placeholder="Correo" required>
            </div>
            <div class="w-full">
              <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Registrar</button>
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
        nombre: '',
        primerApellido: '',
        segundoApellido: '',
        curp: '',
        genero: '',
        tipoSangre: '',
        fechaNacimiento: '',
        telefono: '',
        correo: ''
      };
    },
    methods: {
      register() {
        if (this.contrasena !== this.repetirContrasena) {
          alert("Las contraseñas no coinciden");
          return;
        }
  
        const nuevoUsuario = {
          nombre: this.nombre,
          primerApellido: this.primerApellido,
          segundoApellido: this.segundoApellido,
          curp: this.curp,
          genero: this.genero,
          tipoSangre: this.tipoSangre,
          fechaNacimiento: this.fechaNacimiento,
          telefono: this.telefono,
          correo: this.correo
        };
  
        console.log("Usuario registrado:", nuevoUsuario);
  
        // Aquí puedes agregar la lógica para enviar los datos al backend
      },
      goToLogin() {
        // Lógica para redirigir a la página de inicio de sesión
      }
    }
  };
  </script>
  
  <style scoped>
  /* Aquí puedes agregar estilos específicos para tu componente */
  </style>
  