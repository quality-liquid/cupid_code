<script setup>
import { ref, computed } from 'vue'
import { makeRequest } from './utils/make_request'
import Login from './components/Login.vue'
import SignUp from './components/SignUp.vue'
import Welcome from './components/Welcome.vue'
import DaterHome from './DaterVues/DaterHome.vue'
import ManagerHome from './ManagerVues/ManagerHome.vue'
import CupidHome from './CupidVues/CupidHome.vue'


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



</script>

<template>
  <div id="app">
    <nav class="nav" v-if="!logged_in">
      <a href="#/register"> Sign Up </a>
      <a href="#/login"> Login </a>
      <a href="#/"> Home </a>
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