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
      estatusCirugia: '', // Añadir estatusCirugia en lugar de capacidadMinima
      datosQuirofanos: datosQuirofanos
    };
  },
  computed: {
    quirofanosFiltrados() {
    return this.datosQuirofanos.filter(q => 
      q.estatus.toLowerCase().includes(this.estatusCirugia.toLowerCase())
    );
  }
  },
  methods: {
    actualizarFecha(nuevaFecha) {
      this.fecha = nuevaFecha;
    },
    actualizarFiltro(nuevoEstatus) {
    this.estatusCirugia = nuevoEstatus;
  }
  }
};
</script>
