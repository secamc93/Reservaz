import React from 'react';
import logo from './assets/RZ.png';
import Smart from './assets/Smart.png';
import Formulario from './components/Formulario';
import Reglas from './components/Reglas';

function App() {
  return (
    <div className="bg-gradient-to-b from-green-300 to-blue-300  bg-opacity-50 h-screen flex items-center justify-center">
      <div className="fixed bottom-0 left-0 m-4">
        <img src={logo} className="h-16" alt="logo" />
      </div>
      <div className="fixed bottom-0 right-0 m-4">
        <img src={Smart} className="h-16" alt="smart" />
      </div>
      <div className="fixed top-0 w-full flex justify-center mt-4 z-10">
        <Reglas />
      </div>
      <header>
        <p className="text-2xl font-bold mb-4 text-center">
          Bienvenido a ReservAZ
        </p>
        <div className="backdrop-filter backdrop-blur-md bg-opacity-50 rounded-lg">
          <Formulario />
        </div>
      </header>
    </div>
  );
}

export default App;




