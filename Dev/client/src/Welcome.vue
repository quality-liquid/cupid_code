<script>
import {ref, computed} from 'vue'
import { makeRequest } from './utils/make_request';
// Import login components
const currPath = ref(window.location.hash)

const routes = {
    '#/login': Login,
    '#/signup': Signup,
}

eventListener("hashchange", () => {
  currPath.value = window.location.hash
}) // This will run everytime it's changed to ensure it's correct.

const currView = computed(() => {
  return routes[currPath.value.slice(1) || '/']
}) 

</script>

<template>
  <nav v-for="route in routes" :key="route">
    <a href={{ route }}> {{ chosenRoute[route] }}</a>
  </nav>
  <component :is="currView" />

</template>