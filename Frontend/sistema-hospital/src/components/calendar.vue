<template>
  <div>
    <selector-fecha @fecha-cambiada="actualizarFecha" />
    <filtro-quirofano @filtrar="actualizarFiltro" />
    <tabla-quirofanos
      :fechaSeleccionada="fecha"
      :datosQuirofanos="quirofanosFiltrados"
    />
  </div>
</template>

<script>
import SelectorFecha from './calendar/SelectorFecha.vue';
import FiltroQuirofano from './calendar/FiltroQuirofano.vue';
import TablaQuirofanos from './calendar/TablaQuirofanos.vue';
import datosQuirofanos from '@/assets/quirofanos.json';

export default {
  components: {
    SelectorFecha,
    FiltroQuirofano,
    TablaQuirofanos
  },
  data() {
    return {
      fecha: new Date().toISOString().substr(0, 10),
      capacidadMinima: 1,
      datosQuirofanos: datosQuirofanos
    };
  },
  computed: {
    quirofanosFiltrados() {
      return this.datosQuirofanos.filter(q => q.capacidad >= this.capacidadMinima);
    }
  },
  methods: {
    actualizarFecha(nuevaFecha) {
      this.fecha = nuevaFecha;
    },
    actualizarFiltro(nuevaCapacidad) {
      this.capacidadMinima = nuevaCapacidad;
    }
  }
};
</script>
