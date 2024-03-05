<script setup>
import { ref, computed } from 'vue'
import { makeRequest } from './utils/make_request'
import Login from './components/Login.vue'
import SignUp from './components/SignUp.vue'
import Welcome from './components/Welcome.vue'
import DaterHome from './DaterVues/DaterHome.vue'
import ManagerHome from './ManagerVues/ManagerHome.vue'
import CupidHome from './CupidVues/CupidHome.vue'
import AiChat from './DaterVues/AiChat.vue';
import AiListen from './DaterVues/AiListen.vue';
import CupidCash from './DaterVues/CupidCash.vue';
import Profile from './DaterVues/Profile.vue';

// Variables to display different home views
let currPath = window.location.hash
let logged_in = false;
let type = '';

const routes = {
  '/': Welcome,
  '/register': SignUp,
  '/login': Login,
  '/dater/home': DaterHome,
  '/dater/balance/': CupidCash,
  '/dater/profile/': Profile,
  '/dater/chat/': AiChat,
  '/dater/listen/': AiListen,
  '/manager/home': ManagerHome,
  '/cupid/home': CupidHome,

}


window.addEventListener('hashchange', () => {
  currPath = window.location.hash
  if (currPath.startsWith('/dater') || currPath.startsWith('/cupid') || currPath.startsWith('/manager')) {
    logged_in = true;
    type = currPath.replace('/', '').replace('home', '').toLowerCase();
  }
})

const currentView = computed(() => {
  return routes[currPath.slice(1) || '/' ]
})

function openDrawer() {
  const element = document.getElementById('navbar')
  if (element.className === 'navbar') {
    element.className = 'navbar opened'
  }
  else {
    element.className = 'navbar'
  }
}


async function logout() {
  const result = await makeRequest(`/logout/`)
  logged_in = false
  type = ''
}

</script>

<template>
  <div id="app">
    <nav class="nav" v-if="!logged_in">
      <a href="#/register"> Sign Up </a>
      <a href="#/login"> Login </a>
      <a href="#/"> Home </a>
    </nav>
    <nav class="nav daternav" v-else-if="type.includes('dater')">
      <button @click="openDrawer" class="icon-button">
              <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
      </button>
      <h3>Hello</h3>
      <div id="navbar" class="navbar">
        <a href="#/dater/home"> Home </a>
        <a href="#/dater/profile/"> Profile </a>
        <a href="#/dater/chat/"> AI Chat </a>
        <a href="#/dater/listen/"> AI Listen </a>
        <a href="#/dater/balance/"> Balance</a>
        <a @click="logout"> Logout </a>
      </div>
    </nav>
    <nav class="nav daternav" v-else-if="type.includes('cupid')">
      <button @click="openDrawer" class="icon-button">
              <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
      </button>
      <h3>Hello</h3>
      <div id="navbar" class="navbar">
        <a href="#/cupid/home"> Home </a>
        <a @click="logout"> Logout </a>
      </div>
    </nav>
    <nav class="nav daternav" v-else-if="type.includes('manager')">
      <button @click="openDrawer" class="icon-button">
              <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
      </button>
      <h3>Hello</h3>
      <div id="navbar" class="navbar">
        <a href="#/manager/home"> Home </a>
        <a @click="logout"> Logout </a>
      </div>
    </nav>

    <component :is="currentView" :currPath="currPath"/> 
  </div>
</template>

<style scoped>
  a {
    color: white;
    gap: 10px;
  }
</style>