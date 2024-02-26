<script setup>
import {makeRequest} from '../utils/make_request'
import {ref, computed} from 'vue'

const chosenRoute = ref({});


//Get User and decide which routes to use based on User's Role.
async function getUser() {
  results = await makeRequest();
}

const daterRoutes = {
  '#/dater/home/': Home,
  '#/dater/balance/': Balance,
  '#/dater/profile/': Profile,
  '#/dater/chat/': Chat,
  '#/dater/listen/': Listen,
  '#/dater/calendar/': Calendar,
}

const cupidRoutes = {
  '#/cupid/home/': Home,
  '#/cupid/balance/': Balance,
  '#/cupid/profile/': Profile,
  '#/cupid/gigs/': Gigs,
}

const managerRoutes = {
  '#/manager/home/': Home,
  '#/manager/cupids/': Cupids,
  '#/manager/daters/': Daters
}

const currPath = ref(window.location.hash)

eventListener("hashchange", () => {
  currPath.value = window.location.hash
}) // This will run everytime it's changed to ensure it's correct.

const currView = computed(() => {
  return routes[currPath.value.slice(1) || '/']
}) 

</script>

<template>
  <nav v-for="route in chosenRoute" :key="route">
    <a href={{ route }}> {{ chosenRoute[route] }}</a>
  </nav>
  <component :is="currView" />

</template>
