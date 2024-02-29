<script setup>
import { ref, computed } from 'vue'
import Login from './components/Login.vue'
import SignUp from './components/SignUp.vue'
import Welcome from './components/Welcome.vue'
import UniversalHome from './components/UniversalHome.vue'


const routes = {
  '/': Welcome,
  '/register': SignUp,
  '/login': Login,
  '/home': UniversalHome
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
    <nav class="nav">
      <a href="#/register"> Sign Up </a>
      <a href="#/login"> Login </a>
      <a href="#/"> Back </a>
    </nav>
    <component :is="currentView" :routes="routes" :currPath="currPath"/> 
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