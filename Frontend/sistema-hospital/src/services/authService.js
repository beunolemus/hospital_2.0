import axios from 'axios';


export async function obtenerDatosConToken(token) {
  try {
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6InN0cmluZyIsIkNvcnJlb19FbGVjdHJvbmljbyI6InN0cmluZyIsIkNvbnRyYXNlbmEiOiJzdHJpbmciLCJOdW1lcm9fVGVsZWZvbmljb19Nb3ZpbCI6InN0cmluZyJ9.1tIv5sjC7ltAH08d4Ngyb44Ba-uK2p3LW9_yuYf42qM"

    const response = await axios.get('http://127.0.0.1:8000/cirugias/', {
      headers: {
        
        'Authorization': `Bearer ${token}`  // Incluye el token en los encabezados
      }
    });
    
    return response.data;  // Maneja la respuesta según lo necesites
  } catch (error) {
    console.error('Error al obtener los datos:', error);
    throw error;  // Maneja el error adecuadamente
  }
}
