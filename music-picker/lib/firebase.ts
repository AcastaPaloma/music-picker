// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

import { GoogleAuthProvider } from "firebase/auth";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCopgKfd4QADcvTPGM9QKBEBrH_z5A1FxE",
  authDomain: "music-picker-449aa.firebaseapp.com",
  projectId: "music-picker-449aa",
  storageBucket: "music-picker-449aa.firebasestorage.app",
  messagingSenderId: "677236228426",
  appId: "1:677236228426:web:f934c8d400681366cb01b3",
  measurementId: "G-G8KQXGPY08"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Login 
const provider = new GoogleAuthProvider();

export { app, provider }