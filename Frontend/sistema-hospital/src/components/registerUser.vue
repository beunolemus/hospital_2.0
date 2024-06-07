<template>
  <div class="flex flex-col items-center justify-center p-12">
    <!-- Encabezado y descripción centrados -->
    <div class="text-center mb-8">
      <h2 class="text-2xl font-bold text-[#07074D]">HOSPITAL PRIVILAGE CARE</h2>
      <p class="text-sm text-[#6B7280]">Registrar usuario</p>
    </div>
    <!-- Contenedor del formulario -->
    <div class="max-w-6xl w-full">
      <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto">
        <div class="w-full p-8 lg:w-1/2">
          <Persona />
        </div>
        <div class="w-full p-8 lg:w-1/2">
          <Usuario />
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import Persona from './persona.vue'
import Usuario from './usuario.vue'

export default {
  components: {
    Persona,
    Usuario
  }
}
</script>

<style scoped>
/* Ajusta el ancho máximo y centra el contenedor */
.max-w-6xl {
  max-width: 1200px; /* Ancho máximo */
  margin: 0 auto; /* Centra horizontalmente */
}
</style>
