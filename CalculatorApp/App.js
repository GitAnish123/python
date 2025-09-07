import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function App() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');

  const handlePress = (value) => {
    if (value === '=') {
      try {
        setResult(eval(input).toString());
      } catch {
        setResult('Error');
      }
    } else if (value === 'C') {
      setInput('');
      setResult('');
    } else {
      setInput(input + value);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.result}>{result || input || '0'}</Text>
      <View style={styles.row}>
        {['7', '8', '9', '/'].map((item) => (
          <Button key={item} value={item} onPress={handlePress} />
        ))}
      </View>
      <View style={styles.row}>
        {['4', '5', '6', '*'].map((item) => (
          <Button key={item} value={item} onPress={handlePress} />
        ))}
      </View>
      <View style={styles.row}>
        {['1', '2', '3', '-'].map((item) => (
          <Button key={item} value={item} onPress={handlePress} />
        ))}
      </View>
      <View style={styles.row}>
        {['C', '0', '=', '+'].map((item) => (
          <Button key={item} value={item} onPress={handlePress} />
        ))}
      </View>
    </View>
  );
}

const Button = ({ value, onPress }) => (
  <TouchableOpacity style={styles.button} onPress={() => onPress(value)}>
    <Text style={styles.buttonText}>{value}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  result: {
    fontSize: 40,
    marginBottom: 20,
  },
  row: {
    flexDirection: 'row',
  },
  button: {
    padding: 20,
    margin: 5,
    backgroundColor: '#2196F3',
    borderRadius: 5,
  },
  buttonText: {
    fontSize: 25,
    color: 'white',
  },
});