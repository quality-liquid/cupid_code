import Welcome from './components/Welcome.vue';
import Login from './components/Login.vue';
import SignUp from './components/SignUp.vue';
import UniversalHome from './components/UniversalHome.vue';
import { createRouter, createWebHistory } from 'vue-router';

export const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', name: 'Welcome', component: Welcome },
      { path: '/#/register', name: 'SignUp', component: SignUp },
      { path: '/#/login', name: 'Login', component: Login},
      { path: '/#/home', name: 'Home', component: UniversalHome },
    ],
});