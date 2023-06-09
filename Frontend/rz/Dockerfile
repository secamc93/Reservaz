# Seleccionamos la imagen base
FROM node:14

# Creamos un directorio de trabajo
WORKDIR /app

# Copiamos el archivo package.json y package-lock.json (si existe) en nuestro directorio de trabajo
COPY package*.json ./

# Instalamos las dependencias
RUN npm install

# Copiamos el resto de nuestro código al directorio de trabajo
COPY . .

# Exponemos el puerto que usará nuestra aplicación (3000 en caso de aplicaciones creadas con create-react-app)
EXPOSE 3000

# Ejecutamos nuestra aplicación
CMD ["npm", "start"]

