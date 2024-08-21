<template>
  <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-6xl w-full">
    <h2>Quirófanos disponibles para {{ fechaSeleccionada }}</h2>
    <div class="table-wrapper">
      <table class="fixed-header-table">
        <thead>
          <tr>
            <th>Tipo</th>
            <th>Nombre</th>
            <th>Nivel de Urgencia</th>
            <th>Horario</th>
            <th>Valoración Médica</th>
            <th>Estatus</th>
            <th>Fecha de Registro</th>
            <th>Fecha de Actualización</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="quirofano in quirófanosFiltrados" :key="quirofano.ID">
            <td>{{ quirofano.Tipo }}</td>
            <td>{{ quirofano.Nombre }}</td>
            <td>{{ quirofano.Nivel_Urgencia }}</td>
            <td>{{ new Date(quirofano.Horario).toLocaleString() }}</td>
            <td>{{ quirofano.Valoracion_Medica }}</td>
            <td>{{ quirofano.Estatus }}</td>
            <td>{{ quirofano.Fecha_Registro ? new Date(quirofano.Fecha_Registro).toLocaleString() : '' }}</td>
            <td>{{ quirofano.Fecha_Actualizacion ? new Date(quirofano.Fecha_Actualizacion).toLocaleString() : '' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fechaSeleccionada: {
      type: String,
      required: true
    },
    datosQuirofanos: {
      type: Array,
      required: true
    }
  },
  computed: {
    quirófanosFiltrados() {
      // Filtrar los quirófanos según la fecha seleccionada y el estatus
      return this.datosQuirofanos.filter(q => 
        new Date(q.Horario).toLocaleDateString() === new Date(this.fechaSeleccionada).toLocaleDateString()
      );
    }
  }
};
</script>

<style scoped>
.table-wrapper {
  width: 100%;
  overflow-x: auto;  /* Habilitar el scroll horizontal si el contenido es demasiado ancho */
}

.fixed-header-table {
  width: 100%;
  border-collapse: collapse;
}

.fixed-header-table th, .fixed-header-table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.fixed-header-table thead {
  position: sticky;
  top: 0;
  background-color: #f9f9f9; /* Color de fondo del encabezado */
  z-index: 1;
  overflow: hidden;
  text-overflow: ellipsis; /* Añadir puntos suspensivos si el texto es muy largo */
}

th {
  background-color: #f2f2f2;
  white-space: nowrap; /* Evitar que el texto del encabezado se divida en varias líneas */
}

td {
  white-space: nowrap; /* Evitar que el texto de las celdas se divida en varias líneas */
}
</style>