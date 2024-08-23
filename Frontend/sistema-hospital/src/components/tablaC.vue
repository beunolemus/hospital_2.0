<template>
  <div class="bg-gray-300 rounded-2xl p-10 flex flex-col items-center max-w-6xl w-full">
    <h1 class="font-bold text-3xl text-[#0F6466] mb-4">Registros de Cirugías</h1>

    <div class="w-full mb-4 flex justify-between items-center">
      <button @click="irACrearCirugia" class="bg-gray-500 text-white py-2 px-4 rounded-xl hover:scale-105 duration-300 hover:bg-[#002c7424] font-medium">
        Crear Cirugía
      </button>

      <div class="relative w-full max-w-md">
        <input v-model="busqueda" type="text" class="p-2 rounded-xl border border-gray-300 w-full pr-10" placeholder="Buscar cirugía..." />
        <span class="absolute inset-y-0 right-0 flex items-center px-3 bg-[#0F6466] text-white rounded-r-xl">
          <i class="fas fa-search"></i>
        </span>
      </div>
    </div>

    <div class="w-full overflow-x-auto">
      <table class="w-full table-auto border-collapse border border-gray-300">
        <thead class="bg-gray-200">
          <tr>
            
            <th class="p-2 border-b">Nombre</th>
            <th class="p-2 border-b">Descripción</th>
            <th class="p-2 border-b">Nivel de Urgencia</th>
            <th class="p-2 border-b">Horario</th>
            <th class="p-2 border-b">Observaciones</th>
            <th class="p-2 border-b">Consumible</th>
            <th class="p-2 border-b">Acciones</th> <!-- Columna para botones -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="cirugia in cirugiasFiltradas" :key="cirugia.ID">
            
            <td class="p-2 border-b">{{ cirugia.Nombre }}</td>
            <td class="p-2 border-b">{{ cirugia.Descripcion }}</td>
            <td class="p-2 border-b">{{ cirugia.Nivel_Urgencia }}</td>
            <td class="p-2 border-b">{{ cirugia.Horario }}</td>
            <td class="p-2 border-b">{{ cirugia.Observaciones }}</td>
            <td class="p-2 border-b">{{ cirugia.Consumible }}</td>
            <td class="p-2 border-b text-center">
              <button @click="eliminarCirugia(cirugia.ID)" class="bg-red-500 text-white py-1 px-2 rounded-xl hover:scale-105 duration-300 hover:bg-red-600">
                <i class="fas fa-trash-alt"></i> Eliminar
              </button>
              <button @click="editarCirugia(cirugia.ID)" class="bg-yellow-500 text-white py-1 px-2 rounded-xl hover:scale-105 duration-300 hover:bg-yellow-600">
                <i class="fas fa-edit"></i> Editar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cirugias: [],
      busqueda: '', // Variable para almacenar el texto de búsqueda
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6InN0cmluZyIsIkNvcnJlb19FbGVjdHJvbmljbyI6InN0cmluZyIsIkNvbnRyYXNlbmEiOiJzdHJpbmciLCJOdW1lcm9fVGVsZWZvbmljb19Nb3ZpbCI6InN0cmluZyJ9.1tIv5sjC7ltAH08d4Ngyb44Ba-uK2p3LW9_yuYf42qM' // Reemplaza con tu token real
    };
  },
  computed: {
    cirugiasFiltradas() {
      const searchTerm = this.busqueda.toLowerCase();

      return this.cirugias.filter(cirugia => {
        const tipo = (cirugia.Tipo || '').toString().toLowerCase();
        const nombre = (cirugia.Nombre || '').toString().toLowerCase();
        const descripcion = (cirugia.Descripcion || '').toString().toLowerCase();
        const nivelUrgencia = (cirugia.Nivel_Urgencia || '').toString().toLowerCase();
        const horario = (cirugia.Horario || '').toString().toLowerCase();
        const observaciones = (cirugia.Observaciones || '').toString().toLowerCase();
        const consumible = (cirugia.Consumible || '').toString().toLowerCase();

        return (
          tipo.includes(searchTerm) ||
          nombre.includes(searchTerm) ||
          descripcion.includes(searchTerm) ||
          nivelUrgencia.includes(searchTerm) ||
          horario.includes(searchTerm) ||
          observaciones.includes(searchTerm) ||
          consumible.includes(searchTerm)
        );
      });
    }
  },
  mounted() {
    this.obtenerCirugias();
  },
  methods: {
    irACrearCirugia() {
      this.$router.push({ name: 'crearC' }); // Redirecciona a la vista CrearCirugias
    },
    eliminarCirugia(id) {
      axios.delete(`http://127.0.0.1:8000/cirugia/${id}/`, {
        headers: {
          'Authorization': `Bearer ${this.token}`,
        }
      })
      .then(response => {
        console.log('Response status:', response.status); // Imprime el estado de la respuesta
        // Si la eliminación es exitosa, actualizar la lista de cirugías
        this.obtenerCirugias();
      })
      .catch(error => {
        console.error('Error al eliminar la cirugía:', error.response ? error.response.data : error.message);
      });
    },
    editarCirugia(id) {
      this.$router.push({ name: 'EditCirugia', params: { id: id } });
    },
    obtenerCirugias() {
      axios.get('http://127.0.0.1:8000/cirugias/', {
        headers: {
          'Authorization': `Bearer ${this.token}`,
        }
      })
      .then(response => {
        this.cirugias = response.data; // Asignar los datos a la variable cirugias
      })
      .catch(error => {
        console.error('Error al obtener los datos:', error.response ? error.response.data : error.message);
      });
    }
  }
};
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.table {
  margin-bottom: 0;
}

.table thead th {
  background-color: #4a4c4d; /* Gris claro */
  color: #495057; /* Color del texto para mejor contraste */
}

.bg-gray-100 {
  background-color: #f3f4f6;
}

.bg-gray-300 {
  background-color: #e5e7eb;
}

.bg-gray-500 {
  background-color: #6b7280;
}

.bg-gray-500:hover {
  background-color: #4b5563;
}

.bg-[#0F6466] {
  background-color: #0F6466;
}

.text-[#0F6466] {
  color: #0F6466;
}

.text-white {
  color: #ffffff;
}

.text-gray-300 {
  color: #d1d5db;
}

.table td {
  word-wrap: break-word; /* Ajustar el texto largo */
  max-width: 200px; /* Limitar el ancho máximo de las celdas */
}
</style>
