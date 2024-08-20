<template>
    <div>
      <h2>Quirófanos disponibles para {{ fechaSeleccionada }}</h2>
      <div v-for="quirófano in quirófanos" :key="quirófano.id">
        <h3>{{ quirófano.nombre_quirofano }}</h3>
        <p>Capacidad: {{ quirófano.capacidad }}</p>
        <ul>
          <li v-for="horario in quirófano.disponibilidad" :key="horario.hora">
            {{ horario }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['fechaSeleccionada', 'datosQuirofanos'],
    computed: {
      quirófanos() {
        return this.datosQuirofanos.filter(q => 
          q.disponibilidad.some(d => d.fecha === this.fechaSeleccionada)
        );
      }
    }
  };
  </script>
  