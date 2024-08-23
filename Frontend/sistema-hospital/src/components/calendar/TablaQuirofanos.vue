<template>
  
    <div class="bg-gray-300 rounded-2xl p-10 flex flex-col items-center max-w-6xl w-full">
      <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Quirófanos disponibles para {{ fechaSeleccionada }}</h2>
      <div class="table-wrapper">
        <table class="fixed-header-table">
          <thead class="bg-light">
            <tr>
              <th>Tipo</th>
              <th>Nivel de Urgencia</th>
              <th>Valoración Médica</th>
              <th>Estatus</th>
              <th>Fecha de Registro</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="quirofano in quirófanosFiltrados" :key="quirofano.ID">
              <td>{{ quirofano.Tipo }}</td>
              <td>{{ quirofano.Nivel_Urgencia }}</td>
              <td>{{ quirofano.Valoracion_Medica }}</td>
              <td>{{ quirofano.Estatus }}</td>
              <td>{{ quirofano.Fecha_Registro ? new Date(quirofano.Fecha_Registro).toLocaleString() : '' }}</td>
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
      // Filtrar los quirófanos según la fecha seleccionada
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
  background-color: #4a4c4d; /* Gris oscuro para el encabezado */
  color: #ffffff; /* Texto blanco para el encabezado */
  z-index: 1;
  overflow: hidden;
  text-overflow: ellipsis; /* Añadir puntos suspensivos si el texto es muy largo */
}

th {
  background-color: #4a4c4d; /* Gris oscuro para el encabezado */
  color: #ffffff; /* Texto blanco para el encabezado */
  white-space: nowrap; /* Evitar que el texto del encabezado se divida en varias líneas */
}

td {
  white-space: nowrap; /* Evitar que el texto de las celdas se divida en varias líneas */
}

.bg-gray-100 {
  background-color: #f7f9f9; /* Fondo gris claro para el contenedor principal */
}

.bg-gray-300 {
  background-color: #d2e8e3; /* Fondo gris claro para el contenedor de la tabla */
}

.font-bold {
  font-weight: bold; /* Negrita para los títulos */
}

.text-[#0F6466] {
  color: #0F6466; /* Color personalizado para los textos principales */
}

.mb-4 {
  margin-bottom: 1rem; /* Espaciado inferior */
}

.text-3xl {
  font-size: 1.875rem; /* Tamaño de fuente para títulos grandes */
}
</style>
