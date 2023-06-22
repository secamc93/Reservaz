import React, { useState, useEffect } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import backgroundImage from '../assets/AZ.png';
import  QRCodeSVG  from 'qrcode.react';


function Formulario() {
  const [cedula, setCedula] = useState('');
  const [ruta, setRuta] = useState('');
  const [rutas, setRutas] = useState([]);
  const [valoresEnviados, setValoresEnviados] = useState([]);
  const [respuesta, setRespuesta] = useState(null);
  const [error, setError] = useState(null);
  const [reserva, setReserva] = useState(null);


  useEffect(() => {
    fetch('http://localhost:8000/app1/ruta/')
      .then(response => response.json())
      .then(data => setRutas(data))
      .catch((error) => {
        console.error('Error:', error);
        toast.error('Error al obtener las rutas');
      });
  }, []);

  const handleCedulaChange = (event) => {
    setCedula(event.target.value);
  };

  const handleRutaChange = (event) => {
    setRuta(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Cedula:', cedula);
    console.log('Ruta seleccionada:', ruta);
    setValoresEnviados([cedula, ruta]);

      // Imprimir el JSON antes de enviar la petición
  const requestData = {
    DNI: cedula,
    NombreRuta: ruta
  };
  console.log('JSON a enviar:', JSON.stringify(requestData));

    // hacer la petición HTTP POST aquí
    fetch('http://localhost:8000/app1/reserva/create/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
},
    body: JSON.stringify({
    DNI: Number(cedula),
    NombreRuta: ruta
  })
})
  .then(response => {
    if (!response.ok) {
      // si la respuesta es un error HTTP, convertirla a JSON
      // y lanzar un error que incluya los detalles del error
      return response.json().then(errorData => {
        throw new Error(JSON.stringify(errorData));
      });
    }
    return response.json();
  })
  .then(data => {
    console.log(data); // Mostrar en la consola
    setRespuesta(data); // Almacenar en el estado
    setReserva(data.reserva); // Almacena los datos de la reserva en el estado
    toast.success('Solicitud enviada correctamente');
  })
  .catch((error) => {
    console.error('Error:', error);
    // mostrar el error de validación en la interfaz de usuario
    const errorObject = JSON.parse(error.message);
    let errorMessage;
    if (errorObject.non_field_errors && errorObject.non_field_errors.length > 0) {
        errorMessage = errorObject.non_field_errors[0];
    } else {
        errorMessage = 'Ocurrió un error inesperado';
      }
    toast.error(`${errorMessage}`);
    setError(errorMessage); 
  });

    setCedula('');
    setRuta('');
  };

  return (
    <div className="bg-green-600 bg-opacity-20 bg-center p-4 rounded-lg shadow-lg">
      <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
        <h2 className="text-black text-center mb-4 uppercase font-bold  bg-opacity-80 rounded-md">Formulario de Reserva</h2>
        <label className="text-black  font-bold text-center" >
          Número de cédula:
          <input
            type="number"
            value={cedula}
            onChange={handleCedulaChange}
            className="text-center p-2 bg-white rounded-md w-full"
          />
        </label>
        <label className="text-black font-bold text-center">
          Ruta:
          <select onChange={handleRutaChange} className="text-center mb-6 p-2 bg-white rounded-md w-full">
            <option value="">Selecciona una ruta</option>
            {rutas.map(ruta => 
              <option key={ruta.id} value={ruta.Nombre}>{ruta.Nombre}</option>
            )}
          </select>
        </label>

        <input
          type="submit"
          value="Enviar"
          className="py-2 m-20 bg-yellow-600 hover:bg-green-200 text-black font-bold rounded-md"
        />
      </form>
      {reserva && (
      <div>
        <h2>Datos de la Reserva:</h2>
        <p>ID: {reserva.id}</p>
        <p>DNI: {reserva.DNI}</p>
        <p>Nombre de la Ruta: {reserva.NombreRuta}</p>
        <p>Fecha de Reserva: {new Date(reserva.FechaReserva).toLocaleDateString()}</p>
        <h2>Código QR de la Reserva:</h2>
        <QRCodeSVG value={String(reserva.id)} />
      </div>
)}
      <ToastContainer /> 
    </div>
  );
}

export default Formulario;
