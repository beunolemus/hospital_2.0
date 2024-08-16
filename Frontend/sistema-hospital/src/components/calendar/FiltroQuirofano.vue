<template>
    <div>
      <label for="capacidad">Capacidad mínima:</label>
      <input type="number" v-model="capacidadMinima" @input="filtrarQuirofanos">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        capacidadMinima: 1
      };
    },
    methods: {
      filtrarQuirofanos() {
        this.$emit('filtrar', this.capacidadMinima);
      }
    }
  };
  </script>
  