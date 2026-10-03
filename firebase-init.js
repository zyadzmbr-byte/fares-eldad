// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBRys4lNgZ64RoJBlC9NW-scfO2m-59bcY",
  authDomain: "fares-eldad.firebaseapp.com",
  projectId: "fares-eldad",
  storageBucket: "fares-eldad.firebasestorage.app",
  messagingSenderId: "576584552167",
  appId: "1:576584552167:web:961e3a8d388b3ca38b9c42"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const storage = getStorage(app);

export { db, auth, storage };
