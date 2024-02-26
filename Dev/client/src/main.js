import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import Welcome from './components/Welcome.vue';
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', component: Welcome },
      { path: '/register', component: RegisterPage },
      { path: '/login', component: LoginPage },
      { path: '/dashboard', component: DashboardPage },
    ],
  });


createApp(App).mount('#app')
