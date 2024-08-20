<template>
 <!--  <section class="bg-gray-100 min-h-screen flex justify-center items-center"> -->
    <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-6xl w-full">
   <h2>Quirófanos disponibles para {{ fechaSeleccionada }}</h2>
  <div class="table-wrapper">
    <table class="fixed-header-table">
      <thead>
        <tr>
          <th>Nombre del Quirófano</th>
          <th>Estatus de cirugía</th> <!-- Asegúrate de tener esta columna -->
          <th>Horarios</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="quirófano in quirófanosFiltrados" :key="quirófano.id">
          <td>{{ quirófano.nombre_quirofano }}</td>
          <td>{{ quirófano.estatus }}</td> <!-- Mostrar estatus -->
          <td>
            <ul>
              <li v-for="disponibilidad in quirófano.disponibilidad" :key="disponibilidad.fecha">
                <strong>{{ disponibilidad.fecha }}</strong>: 
                <span v-for="horario in disponibilidad.horarios" :key="horario">{{ horario }}</span>
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<!--   </section> -->
</template>


<script>
export default {
  props: ['fechaSeleccionada', 'datosQuirofanos'],
  computed: {
    quirófanosFiltrados() {
      // Filtrar los quirófanos según la fecha seleccionada
      return this.datosQuirofanos.filter(q => 
        q.disponibilidad.some(d => d.fecha === this.fechaSeleccionada)
      );
    }
  }
};
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

.table-wrapper {
  max-height: 400px; /* Altura máxima del contenedor de la tabla */
  overflow-y: auto;  /* Habilitar el scroll vertical */
  border: 1px solid #ddd;
}

.fixed-header-table {
  width: 100%;
  border-collapse: collapse;
}

.fixed-header-table thead {
  position: sticky;
  top: 0;
  background-color: #f9f9f9; /* Color de fondo del encabezado */
  z-index: 1;
}

.fixed-header-table th,
.fixed-header-table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  white-space: nowrap; /* Evitar que el texto se divida en varias líneas */
}
</style>
