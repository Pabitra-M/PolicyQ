// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: import.meta.env.firebase_apiKey,
  authDomain: "policyq-50e70.firebaseapp.com",
  projectId: "policyq-50e70",
  storageBucket: "policyq-50e70.appspot.com", // ✅ corrected
  messagingSenderId: "708254283573",
  appId: "1:708254283573:web:f137db8927ea8fc3d03e7c",
  measurementId: "G-PQ0YG2K035"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// ✅ Correct export
export const storage = getStorage(app);
