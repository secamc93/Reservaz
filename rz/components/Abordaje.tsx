// components/Abordaje.tsx
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const Abordaje = () => {
  const navigation = useNavigation();

  const handleGoBack = () => {
    navigation.goBack(); // Esto te llevará a la pantalla anterior
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Abordaje</Text>
      <Button title="Inicio" onPress={handleGoBack} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 18,
    color: '#000',
  },
});

export default Abordaje;
