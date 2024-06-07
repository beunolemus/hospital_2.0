<template>
  <section class="bg-gray-100 min-h-screen flex box-border justify-center items-center">
    <div class="bg-[#D2E8E3] rounded-2xl p-5 flex flex-col items-center">
      <div class="w-full max-w-md px-8">
        <h2 class="font-bold text-3xl text-[#0F6466] mb-4 text-center">Registro</h2>
        <p class="text-sm mb-8 text-[#002D74] text-center">Bienvenido al registro de Usuario</p>

        <form @submit.prevent="register" class="flex flex-col gap-4">
          <div class="flex flex-col gap-4 w-full">
            <input class="p-2 rounded-xl border flex-1" type="text" v-model="usuario" placeholder="Usuario" required>
            <input class="p-2 rounded-xl border flex-1" type="password" v-model="contrasena" placeholder="Contraseña" required>
            <input class="p-2 rounded-xl border flex-1" type="password" v-model="repetirContrasena" placeholder="Repetir Contraseña" required>
          </div>
          <div class="w-full flex flex-col items-center gap-2">
            <RouterLink to="/dashboard">
              <button class="bg-[#0593A2] text-white py-2 px-6 rounded-xl hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium" type="submit">Registrar</button>
            </RouterLink>
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
      usuario: '',
      contrasena: '',
      repetirContrasena: ''
    };
  },
  methods: {
    register() {
      if (this.contrasena !== this.repetirContrasena) {
        alert("Las contraseñas no coinciden");
        return;
      }

      const nuevoUsuario = {
        usuario: this.usuario,
        contrasena: this.contrasena
      };

      console.log("Usuario registrado:", nuevoUsuario);

      // Aquí puedes agregar la lógica para enviar los datos al backend
    }
  }
};
</script>

<style scoped>
/* Ajustar tamaño de botones y centrar contenido */

button {
  width: auto;
  min-width: 100px;
}
</style>
