import {createRouter, createWebHashHistory } from 'vue-router';
// General
import Login from '../components/Login.vue'
import Welcome from '../components/Welcome.vue'
import SignUp from '../components/SignUp.vue'
import NotFound from '../components/NotFound.vue'
import DaterHome from '../DaterVues/DaterHome.vue'
import CupidHome from '../CupidVues/CupidHome.vue'
import ManagerHome from '../ManagerVues/ManagerHome.vue'

// Dater specific
import AiChat from '../DaterVues/AiChat.vue';
import AiListen from '../DaterVues/AiListen.vue';
import CupidCash from '../DaterVues/CupidCash.vue';
import DaterProfile from '../DaterVues/DaterProfile.vue';

const routes = [
    {
        path: '/',
        name: 'Welcome',
        component: Welcome
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: SignUp
    },
    {
        path: '/dater/home',
        name: 'Dater Home',
        component: DaterHome
    },
    {
        path: '/dater/chat',
        name: 'AI Chat',
        component: AiChat
    },
    {
        path: '/dater/listen',
        name: 'AI Listen',
        component: AiListen
    },
    {
        path: '/dater/balance',
        name: 'Cupid Cash',
        component: CupidCash
    },
    {
        path: '/dater/profile',
        name: 'Dater Profile',
        component: DaterProfile
    },
    {
        path: '/cupid/home',
        name: 'Cupid Home',
        component: CupidHome
    },
    {
        path: '/manager/home',
        name: 'Manager Home',
        component: ManagerHome
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
