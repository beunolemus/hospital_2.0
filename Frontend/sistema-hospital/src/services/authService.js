import axios from 'axios';


export async function obtenerDatosConToken(token) {
  try {
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOb21icmVfVXN1YXJpbyI6ImJyYXlhbiIsIkNvcnJlb19FbGVjdHJvbmljbyI6ImJyYXlhbkBnbWFpbC5jb20iLCJDb250cmFzZW5hIjoiYnJheWFuMTIzIiwiTnVtZXJvX1RlbGVmb25pY29fTW92aWwiOiI3NDYxMTg2MTQyIn0.UTL4nUvy-WiZAXn9gFJST7BSmWaMOnoi2Ja2HBfsS7A"

    const response = await axios.get('http://127.0.0.1:8000/cirugias/?skip=0&limit=100', {
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
