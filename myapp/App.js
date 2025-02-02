// import { StatusBar } from 'expo-status-bar';
// import { StyleSheet, Text, View } from 'react-native';

// export default function App() {
//   return (
//     <View style={styles.container}>
//       <Text>Hello World!</Text>
//       <StatusBar style="auto" />
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "green",
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
// });


// import libraries
import React from "react";
import { Text, StyleSheet } from "react-native";

// components
const App = () => {
  return (
    <>
      <View style={styles.text}>
        <Text>Meta Brains</Text>
      </View>
    </>
  );
};

// styling
const styles = StyleSheet.create({
  text: {
    flex: 1,
    color:"red",
    backgroundColor: "grey",
    height: 50,
    alignContent: "center",
    justifyContent: "center",
  },
});

// export
export default App;