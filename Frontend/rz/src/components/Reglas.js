import React, { useState } from 'react';

function PestanaDesplegable() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="w-full max-w-md mx-auto">
      <button 
        className=" uppercase font-bold w-full py-3 px-2 bg-green-600 bg-opacity-40 text-black rounded-lg focus:outline-none focus:shadow-outline"
        onClick={() => setIsOpen(!isOpen)}
      >
        Reglas de las Reservas
      </button>
      {isOpen && (
        <div className=" fixed top-8 bottom-8 left-80 right-80 h-[80vh] mt-16 p-2 bg-white rounded-lg shadow-2x1 overflow-y-auto">
          <h2 className="text-2xl mb-4">Reglas de las Reservas</h2>
          <p className="text-justify text-lg">
            ¡Bienvenido a nuestra página web de reservas de rutas universitarias!
            <br /><br />
            Aquí podrás reservar tu puesto en la ruta que te llevará desde tu casa a la universidad, o viceversa. ¡Es muy sencillo! Solo necesitas tener a mano tu número de cédula y seguir las reglas de reserva que te explicaremos a continuación:
            <br /><br />
            1. Para las rutas en la jornada de la mañana, podrás hacer tu reserva únicamente un día antes. De esta manera, garantizamos que todos los estudiantes tengan la oportunidad de reservar con anticipación.
            <br /><br />
            2. Para las rutas en la noche, podrás hacer tu reserva desde el mediodía anterior hasta el mediodía del mismo día. Así te brindamos flexibilidad para ajustar tus horarios y asegurarte un puesto en la ruta.
            <br /><br />
            Es importante tener en cuenta que si la ruta está llena, recibirás un mensaje indicando que la ruta está completa y no podrás realizar la reserva en ese momento. Te recomendamos revisar regularmente la disponibilidad de las rutas y realizar tu reserva con la debida antelación.
            <br /><br />
            En caso de que no figure en nuestra base de datos de reservas, recibirás un mensaje indicando que no se encontró tu información. Asegúrate de ingresar correctamente tu número de cédula y, si persiste el problema, te recomendamos contactar a nuestro equipo de soporte para ayudarte a resolverlo.
            <br /><br />
            Una vez que realices una reserva exitosa, recibirás un código QR único. Este código será tu certificado de reserva y deberás mostrarlo al conductor de la ruta para verificar tu reserva al momento de abordar. Asegúrate de tener tu código QR siempre a mano.
            <br /><br />
            Estamos comprometidos en brindarte un servicio eficiente y seguro para tu traslado universitario. ¡Realiza tu reserva ahora y asegura tu puesto en la ruta deseada!
            <br /><br />
            Sitienes alguna pregunta o necesitas asistencia adicional, no dudes en contactar a nuestro equipo de soporte, estaremos encantados de ayudarte.
            <br /><br />
            ¡Te deseamos un excelente viaje hacia la universidad!
          </p>
        </div>
      )}
    </div>
  );
}

export default PestanaDesplegable;






