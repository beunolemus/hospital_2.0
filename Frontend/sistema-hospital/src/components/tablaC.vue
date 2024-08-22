<template>
  <div class="container mt-4">
    <!-- Título centrado, más grande y en negrita -->
    <h1 class="text-center mb-4 font-weight-bold" style="font-size: 36px;">Tabla de Cirugías</h1>
    
    <div class="d-flex justify-content-between mb-3">
      <!-- Botón para crear cirugía alineado a la derecha -->
      <button @click="irACrearCirugia" class="btn btn-secondary">Crear Cirugía</button>
      
      <!-- Barra de búsqueda centrada y con color verde -->
      <div class="input-group" style="max-width: 400px;">
        <input v-model="busqueda" type="text" class="form-control" placeholder="Buscar cirugía..." />
        <span class="input-group-text bg-success text-white">
          <i class="fas fa-search"></i>
        </span>
      </div>
    </div>
    
    <table class="table table-bordered">
      <thead class="bg-light">
        <tr>
          <th class="blue-column">Id de la Cirugía</th>
          <th>Paciente_ID</th>
          <th>Espacio_Medico_ID</th>
          <th>Tipo</th>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Nivel de Urgencia</th>
          <th>Horario</th>
          <th>Observaciones</th>
          <th>Estatus</th>
          <th>Consumible</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cirugia in cirugiasFiltradas" :key="cirugia.ID">
          <td class="blue-column">{{ cirugia.ID }}</td>
          <td>{{ cirugia.Paciente_ID }}</td>
          <td>{{ cirugia.Espacio_Medico_ID }}</td>
          <td>{{ cirugia.Tipo }}</td>
          <td>{{ cirugia.Nombre }}</td>
          <td>{{ cirugia.Descripcion }}</td>
          <td>{{ cirugia.Nivel_Urgencia }}</td>
          <td>{{ cirugia.Horario }}</td>
          <td>{{ cirugia.Observaciones }}</td>
          <td>{{ cirugia.Estatus }}</td>
          <td>{{ cirugia.Consumible }}</td>
          <td>
            <button @click="eliminarCirugia(cirugia.ID)" class="btn btn-danger btn-sm">
              <i class="fas fa-trash-alt"></i> Eliminar
            </button>
            <button @click="editarCirugia(cirugia.ID)" class="btn btn-warning btn-sm">
              <i class="fas fa-edit"></i> Editar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cirugias: [],
      busqueda: '', // Variable para almacenar el texto de búsqueda
      token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6InN0cmluZyIsIkNvcnJlb19FbGVjdHJvbmljbyI6InN0cmluZyIsIkNvbnRyYXNlbmEiOiJzdHJpbmciLCJOdW1lcm9fVGVsZWZvbmljb19Nb3ZpbCI6InN0cmluZyJ9.1tIv5sjC7ltAH08d4Ngyb44Ba-uK2p3LW9_yuYf42qM', // Reemplaza con tu token real
    };
  },
  computed: {
    cirugiasFiltradas() {
    const searchTerm = this.busqueda.toLowerCase();

    // Convertir el término de búsqueda a cadena para comparar
    return this.cirugias.filter(cirugia => {
      // Convertir los valores a cadenas y hacer la comparación
      const pacienteId = (cirugia.Paciente_ID !== undefined && cirugia.Paciente_ID !== null) ? cirugia.Paciente_ID.toString().toLowerCase() : '';
      const espacioMedicoId = (cirugia.Espacio_Medico_ID !== undefined && cirugia.Espacio_Medico_ID !== null) ? cirugia.Espacio_Medico_ID.toString().toLowerCase() : '';
      const tipo = (cirugia.Tipo || '').toString().toLowerCase();
      const nombre = (cirugia.Nombre || '').toString().toLowerCase();
      const descripcion = (cirugia.Descripcion || '').toString().toLowerCase();
      const nivelUrgencia = (cirugia.Nivel_Urgencia || '').toString().toLowerCase();
      const estatus = (cirugia.Estatus || '').toString().toLowerCase();
      const consumible = (cirugia.Consumible || '').toString().toLowerCase();

      return (
        pacienteId.includes(searchTerm) ||
        espacioMedicoId.includes(searchTerm) ||
        tipo.includes(searchTerm) ||
        nombre.includes(searchTerm) ||
        descripcion.includes(searchTerm) ||
        nivelUrgencia.includes(searchTerm) ||
        estatus.includes(searchTerm) ||
        consumible.includes(searchTerm)
      );
    });
  },
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
      this.$router.push({ name: 'editarC', params: { id: id } });
    },
    obtenerCirugias() {
      axios.get('http://127.0.0.1:8000/cirugias/?skip=0&limit=100', {
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
/* Estilos para iconos de Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Estilos para la barra de búsqueda centrada y con color verde */
.input-group-text {
  background-color: #243e2a; /* Color verde de Bootstrap */
  color: rgb(66, 76, 75);
}

.form-control {
  border-right: none;
}

.table {
  margin-bottom: 0;
}

.table thead th {
  background-color: #4a4c4d; /* Gris claro */
  color: #495057; /* Color del texto para mejor contraste */
}

/* Fondo azul bajito para la primera columna */
.blue-column {
  background-color: #220c50; /* Azul bajito */
}
</style>
