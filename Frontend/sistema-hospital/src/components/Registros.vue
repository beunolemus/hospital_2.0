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
import { obtenerDatosConToken } from '@/services/authService.js'; // Asegúrate de ajustar el path

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
      datosQuirofanos: []
    };
  },
  computed: {
    quirofanosFiltrados() {
      // Filtrar los quirófanos según la fecha seleccionada y el estatus
      return this.datosQuirofanos.filter(q => 
        new Date(q.Horario).toLocaleDateString() === new Date(this.fecha).toLocaleDateString() &&
        q.Estatus.toLowerCase().includes(this.estatusCirugia.toLowerCase())
      );
    }
  },
  async created() {
    try {
      const response = await obtenerDatosConToken();
      this.datosQuirofanos = response; // Asegúrate de que el formato de respuesta sea un array de objetos
      console.log(response)
    } catch (error) {
      console.error('Error al obtener los datos:', error);
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