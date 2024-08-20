<template>
  <div class="text-center mx-auto">
    <label for="estatus">Estatus de cirugía:</label><br>
    <select type="text" v-model="estatusCirugia" @change="filtrarQuirofanos" class="mt-2">
      <option value="">Todos</option>
      <option value="Programada">Programada</option>
      <option value="En Curso">En Curso</option>
      <option value="Completada">Completada</option>
      <option value="Cancelada">Cancelada</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      estatusCirugia: '' // Cambiado de capacidadMinima a estatusCirugia
    };
  },
  methods: {
    filtrarQuirofanos() {
      this.$emit('filtrar', this.estatusCirugia);
    }
  }
};
</script>
