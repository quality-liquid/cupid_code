<script setup>
import {makeRequest} from '../utils/make_request.js'
import {ref, computed} from 'vue'
import CupidHome from '../CupidVues/CupidHome.vue';
import DaterHome from '../DaterVues/DaterHome.vue';


const chosenRoute = ref('');

//Get User and decide which routes to use based on User's Role.
async function getUser() {
  const results = await makeRequest(`/api/user/`);
  chosenRoute = results.role
}

const currPath = ref(window.location.hash)

const routes = {
  '#/dater/home': DaterHome,
  '#/cupid/home': CupidHome,
  //'#/manager/home': ManagerHome
}

const currView = computed(() => {
  if (chosenRoute === 'dater') return currPath.value = routes['#/dater/home']
  else if (chosenRoute === 'cupid') return currPath.value = routes['#/cupid/home']
})


window.addEventListener("hashchange", () => {
  currPath.value = window.location.hash
}) // This will run everytime it's changed to ensure it's correct.

</script>

<template>
  <component :is="currView" />
</template>

<style>
  h1 {
    margin: 20px;
  }
</style>