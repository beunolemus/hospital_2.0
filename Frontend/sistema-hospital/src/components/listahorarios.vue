<template>
  <section class="bg-gray-100 min-h-screen flex justify-center items-center">
    <div class="bg-[#D2E8E3] rounded-2xl p-10 flex flex-col items-center max-w-6xl w-full overflow-x-auto">
      <div class="w-full px-4">
        <h2 class="font-bold text-3xl text-[#0F6466] mb-4">Lista de Horarios</h2>
        <p class="text-sm mb-8 text-[#002D74]">Revisa y gestiona los horarios</p>

        <div class="overflow-x-auto w-full">
          <table class="w-full table-auto bg-white rounded-xl shadow-lg">
            <thead>
              <tr class="bg-[#0593A2] text-black">
                <th class="py-2 px-4">ID</th>
                <th class="py-2 px-4">Empleado ID</th>
                <th class="py-2 px-4">Nombre</th>
                <th class="py-2 px-4">Especialidad</th>
                <th class="py-2 px-4">Día</th>
                <th class="py-2 px-4">Hora Inicio</th>
                <th class="py-2 px-4">Hora Fin</th>
                <th class="py-2 px-4">Turno</th>
                <th class="py-2 px-4">Departamento</th>
                <th class="py-2 px-4">Sala</th>
                <th class="py-2 px-4">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(horario, index) in horarios" :key="index" class="text-[#002D74] hover:bg-[#D2E8E3]">
                <td class="border-t py-2 px-4">{{ horario.horario_id }}</td>
                <td class="border-t py-2 px-4">{{ horario.empleado_id }}</td>
                <td class="border-t py-2 px-4">{{ horario.nombre }}</td>
                <td class="border-t py-2 px-4">{{ horario.especialidad }}</td>
                <td class="border-t py-2 px-4">{{ horario.dia_semana }}</td>
                <td class="border-t py-2 px-4">{{ horario.hora_inicio }}</td>
                <td class="border-t py-2 px-4">{{ horario.hora_fin }}</td>
                <td class="border-t py-2 px-4">{{ horario.turno }}</td>
                <td class="border-t py-2 px-4">{{ horario.nombre_departamento }}</td>
                <td class="border-t py-2 px-4">{{ horario.nombre_sala }}</td>
                <td class="border-t py-2 px-4">
                  <button class="bg-[#0F6466] text-white py-1 px-2 rounded-md hover:bg-[#0593A2] duration-200" @click="editHorario(horario.horario_id)">Editar</button>
                  <button class="bg-red-500 text-white py-1 px-2 rounded-md hover:bg-red-700 duration-200 ml-2" @click="confirmDelete(horario.horario_id)">Eliminar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="w-full mt-8">
          <button class="bg-[#0593A2] text-white py-2 rounded-xl w-full hover:scale-105 duration-300 hover:bg-[#0F6466] font-medium" @click="goToCreate">Crear Nuevo Horario</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      horarios: [
        {
          horario_id: 1,
          empleado_id: 101,
          nombre: 'Mañana',
          especialidad: 'Cardiología',
          dia_semana: 'Lunes',
          hora_inicio: '08:00',
          hora_fin: '12:00',
          turno: 'Matutino',
          nombre_departamento: 'Cardiología',
          nombre_sala: 'Sala 1'
        },
        {
          horario_id: 2,
          empleado_id: 102,
          nombre: 'Tarde',
          especialidad: 'Neurología',
          dia_semana: 'Martes',
          hora_inicio: '13:00',
          hora_fin: '17:00',
          turno: 'Vespertino',
          nombre_departamento: 'Neurología',
          nombre_sala: 'Sala 2'
        },
        {
          horario_id: 3,
          empleado_id: 103,
          nombre: 'Noche',
          especialidad: 'Pediatría',
          dia_semana: 'Miércoles',
          hora_inicio: '18:00',
          hora_fin: '22:00',
          turno: 'Nocturno',
          nombre_departamento: 'Pediatría',
          nombre_sala: 'Sala 3'
        },
        {
          horario_id: 4,
          empleado_id: 104,
          nombre: 'Mañana',
          especialidad: 'Oncología',
          dia_semana: 'Jueves',
          hora_inicio: '07:00',
          hora_fin: '11:00',
          turno: 'Matutino',
          nombre_departamento: 'Oncología',
          nombre_sala: 'Sala 4'
        },
        {
          horario_id: 5,
          empleado_id: 105,
          nombre: 'Tarde',
          especialidad: 'Gastroenterología',
          dia_semana: 'Viernes',
          hora_inicio: '14:00',
          hora_fin: '18:00',
          turno: 'Vespertino',
          nombre_departamento: 'Gastroenterología',
          nombre_sala: 'Sala 5'
        },
        {
          horario_id: 6,
          empleado_id: 106,
          nombre: 'Noche',
          especialidad: 'Dermatología',
          dia_semana: 'Sábado',
          hora_inicio: '19:00',
          hora_fin: '23:00',
          turno: 'Nocturno',
          nombre_departamento: 'Dermatología',
          nombre_sala: 'Sala 6'
        },
        {
          horario_id: 7,
          empleado_id: 107,
          nombre: 'Mañana',
          especialidad: 'Cirugía General',
          dia_semana: 'Domingo',
          hora_inicio: '08:00',
          hora_fin: '12:00',
          turno: 'Matutino',
          nombre_departamento: 'Cirugía General',
          nombre_sala: 'Sala 7'
        }
      ]
    };
  },
  methods: {
    editHorario(horario_id) {
      window.location.href = `http://localhost:5173/edithorario?id=${horario_id}`;
    },
    confirmDelete(horario_id) {
      if (confirm("¿Estás seguro de que deseas eliminar este horario?")) {
        this.deleteHorario(horario_id);
      }
    },
    deleteHorario(horario_id) {
      console.log("Horario eliminado con ID:", horario_id);
      // Aquí puedes agregar la lógica para eliminar el horario del backend y actualizar la lista de horarios
    },
    goToCreate() {
      window.location.href = 'http://localhost:5173/horarios';
    }
  }
};
</script>

<style scoped>
/* Estilos personalizados para el componente */
table {
  border-collapse: collapse;
}

th, td {
  border-bottom: 1px solid #ccc;
}

tbody tr:hover {
  background-color: #D2E8E3;
}
</style>
