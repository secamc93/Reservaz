// components/Home.tsx
import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';

const Home = () => {
  return (
    <View style={styles.container}>
      <View style={styles.textBackground}>
        <Text style={styles.text}>Bienvenido a Reservaz</Text>
      </View>
      <Image
        source={require('../assets/RZ.png')}
        style={styles.image}
        resizeMode="contain"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#90EE90', // Este es un verde claro
    alignItems: 'center',
    justifyContent: 'center',
  },
  textBackground: {
    backgroundColor: 'white',
    borderRadius: 10,
    paddingHorizontal: 10,
    paddingVertical: 5,
    marginBottom: 20, // Esto proporciona un espacio entre el texto y la imagen
  },
  text: {
    fontSize: 20,
    color: 'black',
  },
  image: {
    width: 200, // Puedes ajustar el tamaño según sea necesario
    height: 200, // Puedes ajustar el tamaño según sea necesario
  },
});

export default Home;
