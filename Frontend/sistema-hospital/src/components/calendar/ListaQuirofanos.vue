<template>
    <div>
      <h2>Quirófanos disponibles para {{ fechaSeleccionada }}</h2><br>
      <div v-for="quirofano in quirofanos" :key="quirofano.ID">
        <h3>{{ quirofano.nombre_quirofano }}</h3>
        <ul>
          <li v-for="horario in quirofano.horario" :key="horario.hora">
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
          q.horario.some(d => d.fecha === this.fechaSeleccionada)
        );
      }
    }
  };
  </script>
  