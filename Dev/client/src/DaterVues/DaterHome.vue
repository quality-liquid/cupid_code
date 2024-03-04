<script setup>
import {ref, computed} from 'vue';
import AiChat from './AiChat.vue';
import AiListen from './AiListen.vue';
import CupidCash from './CupidCash.vue';
import Profile from './Profile.vue';


const routes = {
  '#/dater/home/': DaterHome,
  '#/dater/balance/': CupidCash,
  '#/dater/profile/': Profile,
  '#/dater/chat/': AiChat,
  '#/dater/listen/': AiListen,
  //'#/dater/calendar/': Calendar,
}

const currPath = ref(window.location.hash)

window.addEventListener("hashchange", () => {
  currPath.value = window.location.hash
}) // This will run everytime it's changed to ensure it's correct.

const currView = computed(() => {
  return routes[currPath.value.slice(1) || '/#/dater/home']
}) 

</script>

<template>
  <nav class="nav">
    Page user is on
    <div class="navbar">
      <a href="#/dater/home"> Home </a>
      <a href="#/dater/profile/"> Profile </a>
      <a href="#/dater/chat/"> AI Chat </a>
      <a href="#/dater/listen/"> AI Listen </a>
      <a href="#/dater/balance/"> Balance</a>
      <a href="">Back</a>
    </div>
  </nav>
  <component :is="currView" />
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

  .navbar {
    height: 100%;
    width: 0;
    position: fixed; 
    z-index: 1;
    top: 0; 
    left: 0;
    background-color: #111;
    overflow-x: hidden; 
    padding-top: 60px; 
    transition: 0.5s; 
  }

</style>