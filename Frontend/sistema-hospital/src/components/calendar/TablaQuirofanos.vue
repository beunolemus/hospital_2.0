<template>
  <div>
    <h2>Quirófanos disponibles para {{ fechaSeleccionada }}</h2>
    <table>
      <thead>
        <tr>
          <th>Nombre del Quirófano</th>
          <th>Capacidad</th>
          <th>Estatus de cirugia</th>
          <th>Horarios Disponibles</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="quirófano in quirófanosFiltrados" :key="quirófano.id">
          <td>{{ quirófano.nombre_quirofano }}</td>
          <td>{{ quirófano.capacidad }}</td>
          <td>
            aqui va el estatus de la cirugia
          </td>
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
</style>
