<template>
  <div class="container">
    <div class="columns-3">
      <!-- Tabla de simbología -->
      <div class="legend">
        <div class="legend-item">
          <div class="legend-color available"></div>
          <div class="legend-label">Quirofano disponible</div>
        </div>
        <div class="legend-item">
          <div class="legend-color busy"></div>
          <div class="legend-label">Quirofano ocupado</div>
        </div>
      </div>
      <!-- Fin de tabla de simbología -->

      <!-- Tabla de quirofanos -->
      <div class="quirofano-table">
        <h2>Estado de los Quirofanos</h2>
        <table>
          <thead>
            <tr>
              <th>Quirofano</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(quirofano, index) in quirofanos" :key="index">
              <td>Quirofano {{ index + 1 }}</td>
              <td :class="[quirofano.estado ? 'available' : 'busy']">{{ quirofano.estado ? 'Disponible' : 'Ocupado' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Fin de tabla de quirofanos -->
    </div>

    <!-- Calendario -->
    <div class="calendar-container">
      <h1 class="title">Calendario</h1>
      <div class="calendar">
        <div class="header">
          <button @click="prevMonth">&lt;</button>
          <div class="month">{{ monthNames[currentMonth] }} {{ currentYear }}</div>
          <button @click="nextMonth">&gt;</button>
        </div>
        <div class="weekdays">
          <div class="weekday" v-for="day in weekDays" :key="day">{{ day }}</div>
        </div>
        <div class="days">
          <div
            v-for="day in daysInMonth"
            :key="day.date"
            :class="['day', { today: isToday(day.date), selected: isSelected(day.date) }]"
            @click="selectDate(day.date)"
          >
            {{ day.number }}
          </div>
        </div>
      </div>
    </div>
    <!-- Fin de Calendario -->
  </div>
</template>

<script>
export default {
  name: 'CombinedComponent',
  data() {
    return {
      currentYear: new Date().getFullYear(),
      currentMonth: new Date().getMonth(),
      selectedDate: new Date(),
      weekDays: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
      monthNames: [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
      ],
      quirofanos: [
        { estado: true }, // Quirofano disponible
        { estado: false }, // Quirofano ocupado
        { estado: true }, // Quirofano disponible
        { estado: true }, // Quirofano disponible
        // Puedes agregar más quirofanos según sea necesario
      ],
    };
  },
  computed: {
    daysInMonth() {
      const days = [];
      const firstDay = new Date(this.currentYear, this.currentMonth, 1).getDay();
      const lastDate = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();

      for (let i = 0; i < firstDay; i++) {
        days.push({ number: '', date: null });
      }

      for (let i = 1; i <= lastDate; i++) {
        days.push({ number: i, date: new Date(this.currentYear, this.currentMonth, i) });
      }

      return days;
    },
  },
  methods: {
    prevMonth() {
      if (this.currentMonth === 0) {
        this.currentMonth = 11;
        this.currentYear--;
      } else {
        this.currentMonth--;
      }
    },
    nextMonth() {
      if (this.currentMonth === 11) {
        this.currentMonth = 0;
        this.currentYear++;
      } else {
        this.currentMonth++;
      }
    },
    selectDate(date) {
      this.selectedDate = date;
    },
    isToday(date) {
      const today = new Date();
      return date && date.toDateString() === today.toDateString();
    },
    isSelected(date) {
      return date && date.toDateString() === this.selectedDate.toDateString();
    },
  },
};
</script>

<style scoped>
/* Estilos para la tabla de simbología */
.legend {
  display: flex;
  margin-bottom: 20px;
}

.legend-item {
  display: flex;
  align-items: center;
  margin-right: 20px;
}

.legend-color {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  margin-right: 5px;
}

.available {
  background-color: green;
}

.busy {
  background-color: red;
}

/* Estilos para la tabla de quirofanos */
.quirofano-table {
  margin-top: 20px;
}

.quirofano-table table {
  width: 100%;
  border-collapse: collapse;
}

.quirofano-table th,
.quirofano-table td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

.quirofano-table th {
  background-color: #f2f2f2;
}

.quirofano-table td.available {
  background-color: green;
}

.quirofano-table td.busy {
  background-color: red;
}

/* Estilos para el calendario */
.calendar-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: 0 auto;
}

.title {
  font-size: 2em;
  color: #ff6600;
  margin-bottom: 20px;
  text-align: center;
}

.calendar {
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.header button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
}

.header button:hover {
  background-color: #0056b3;
}

.month {
  font-size: 1.2em;
  font-weight: bold;
  color: #333;
}

.weekdays {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.weekday {
  width: 14%;
  text-align: center;
  font-weight: bold;
  color: #666;
}

.days {
  display: flex;
  flex-wrap: wrap;
}

.day {
  width: 14%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border-radius: 4px;
  margin-bottom: 5px;
}

.day:hover {
  background-color: #eee;
}

.today {
  background-color: #ffcc00;
}

.selected {
  background-color: #007bff;
  color: white;
}
</style>
