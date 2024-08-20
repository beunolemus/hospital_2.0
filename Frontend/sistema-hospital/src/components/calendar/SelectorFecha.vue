<template>
    <div class="text-center mx-auto">
      <label for="fecha">Selecciona una fecha:</label><br>
      <input type="date" v-model="fechaSeleccionada" @change="emitirFecha">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        fechaSeleccionada: new Date().toISOString().substr(0, 10)
      };
    },
    methods: {
      emitirFecha() {
        this.$emit('fecha-cambiada', this.fechaSeleccionada);
      }
    }
  };
  </script>
  