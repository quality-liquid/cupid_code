import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import Welcome from './components/Welcome.vue';
import Login from './components/Login.vue';
import SignUp from './components/SignUp.vue';
import UniversalHome from './components/UniversalHome.vue';
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', component: Welcome },
      { path: '/register', component: SignUp },
      { path: '/login', component: Login },
      { path: '/home', component: UniversalHome },
    ],
});


createApp(App).mount('#app')
