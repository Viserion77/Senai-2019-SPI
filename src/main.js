import Vue from 'vue';
import { initializeApp } from 'firebase/app';
import App from './App.vue';
import vuetify from './plugins/vuetify';
// Import the functions you need from the SDKs you need
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyAXSuCpHhML_4uIG5fTBr4TWME00cY8zj8',
  authDomain: 'prova-web-79fe7.firebaseapp.com',
  projectId: 'prova-web-79fe7',
  storageBucket: 'prova-web-79fe7.appspot.com',
  messagingSenderId: '627864264745',
  appId: '1:627864264745:web:3eff972af6f8b8d9843c38',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
console.log(app);

Vue.config.productionTip = false;

new Vue({
  vuetify,
  render(h) { return h(App); },
}).$mount('#app');
