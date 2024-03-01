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
<nav>
    
</nav>
<component :is="currView" />
</template>

<style scoped>

</style>