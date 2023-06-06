import React, { useState } from 'react';
import backgroundImage from '../assets/AZ.png';


function Formulario() {
  const [cedula, setCedula] = useState('');
  const [ruta, setRuta] = useState('');
  const [valoresEnviados, setValoresEnviados] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Cedula:', cedula);
    console.log('Ruta seleccionada:', ruta);
    setValoresEnviados([cedula, ruta]);
    setCedula('');
    setRuta('');
  };

  const handleCedulaChange = (event) => {
    setCedula(event.target.value);
  };

  const handleRutaChange = (event) => {
    setRuta(event.target.value);
  };

  return (
    <div  className="bg-green-600 bg-opacity-60 bg-center p-4 rounded-lg shadow-lg">
      <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
        <h2 className="text-black text-center mb-4 uppercase font-bold bg-yellow-600 bg-opacity-80 rounded-md">Formulario de Reserva</h2>
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
            <option value="ruta1">Ruta 1</option>
            <option value="ruta2">Ruta 2</option>
            <option value="ruta3">Ruta 3</option>
          </select>
        </label>

        <input
          type="submit"
          value="Enviar"
          className="py-2 m-20 bg-yellow-600 hover:bg-green-200 text-black font-bold rounded-md"
        />
      </form>
      <div className="mt-2 text-center text-white">
        {valoresEnviados.length > 0 && (
          <div>
            <h2>Valores enviados:</h2>
            <p>Cédula: {valoresEnviados[0]}</p>
            <p>Ruta seleccionada: {valoresEnviados[1]}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Formulario;
