<script setup>
import { ref, computed } from 'vue'
import Login from './components/Login.vue'
import SignUp from './components/SignUp.vue'
import Welcome from './components/Welcome.vue'
import DaterHome from './DaterVues/DaterHome.vue'
import ManagerHome from './ManagerVues/ManagerHome.vue'
import CupidHome from './CupidVues/CupidHome.vue'

// Variables to display different home views
let logged_in = false;
let type = '';

const routes = {
  '#/': Welcome,
  '#/register': SignUp,
  '#/login': Login,
  '#/dater/home': DaterHome,
  '#/manager/home': ManagerHome,
  '#/cupid/home': CupidHome
}

const currPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currPath.value.slice(1) || '/' ]
})

</script>

<template>
  <div id="app">
    <nav class="nav" v-if="!logged_in">
      <a href="#/register"> Sign Up </a>
      <a href="#/login"> Login </a>
      <a href="#/"> Home </a>
    </nav>
    <component :is="currentView"/> 
  </div>
</template>

<style scoped>
  .nav {
    color: white;
    background-color: var(--primary-blue);
    top: 0;
    left: 0;
    right: 0; 
    display: flex;
    position: absolute;
    justify-content: space-evenly;
    align-items: center;
    padding: 8px 16px;
  }

  a {
    color: white;
    gap: 10px;
  }
</style>