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
import DepositMoney from '../DaterVues/DepositMoney.vue';

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
        path: '/dater/home/:id',
        name: 'DaterHome',
        component: DaterHome,
    },
    {
        path: '/dater/chat/:id',
        name: 'AiChat',
        component: AiChat
    },
    {
        path: '/dater/listen/:id',
        name: 'AiListen',
        component: AiListen
    },
    {
        path: '/dater/balance/:id',
        name: 'CupidCash',
        component: CupidCash
    },
    {
        path: '/dater/add-money/:id/:amt',
        name: 'AddMoney',
        component: DepositMoney
    },
    {
        path: '/dater/profile/:id',
        name: 'DaterProfile',
        component: DaterProfile
    },
    {
        path: '/cupid/home',
        name: 'CupidHome',
        component: CupidHome,
    },
    {
        path: '/manager/home',
        name: 'ManagerHome',
        component: ManagerHome,
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
