import React from 'react';
import logo from './assets/RZ.png';
import Formulario from './components/Formulario';

function App() {
  return (
    <div className="bg-gradient-to-b from-green-300 to-blue-300  bg-opacity-50 h-screen flex items-center justify-center">
      <div className="fixed top-0 left-0 m-4">
        <img src={logo} className="h-16" alt="logo" />
      </div>
      <header>
        <p className="text-2xl font-bold mb-4 text-center">
          Bienvenido a Reservaz
        </p>
        <Formulario />
      </header>
    </div>
  );
}

export default App;

