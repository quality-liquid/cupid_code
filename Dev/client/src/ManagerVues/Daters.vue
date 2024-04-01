<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

const daters = ref([{ }])
const daterCount = ref(0)

const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router
// Open and closes drawer w/ shorthand
function openDrawer() {
  const element = document.getElementById('navbar')
  if (element.className === 'navbar') {
    element.className = 'navbar opened'
  }
  else {
    element.className = 'navbar'
  }
}
// Logout function
async function logout() {
  const result = await makeRequest(`/logout/`)
  router.push('/')
}

async function getDaters() {
  const res = await makeRequest('/api/manager/daters/')
  daters.value = res
}
  
async function suspend() {
  const header = document.getElementById('header')
  if (header.attributes[2].value.includes('suspended')) header.setAttribute('class', 'header')
  else header.setAttribute('class', 'header suspended')
}

onMounted(getDaters)
</script>

<template>
  <!-- nav banner component -->
  <!-- end nav bar -->
  <nav class="nav homenav">
      <button @click="openDrawer" class="icon-button">
          <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
      </button>
      <span>Dater Information</span>
      <img :src="'/get_heart/'" alt="Heart" class="icon">
      <div id="navbar" class="navbar">
          <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
          <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
          <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
          <button class="logout" @click="logout"> Logout </button>
      </div>
  </nav>
  <figure>{{ daterCount }} Daters</figure>

  <!-- header & button need turnary stuff to swap between suspend/unsuspend -->
  <div v-for="dater of daters" class="container">
    <div class="header" id="header">
      <img :src="'/get_temp_pfp/'" alt="Profile Picture" class="icon">
      <h4>Name</h4>
    </div>
    <article class="user-data" id="user-data">
      <span>Rating: {{ dater.rating_sum }}</span>
      <span>Location: {{ dater.location }}</span>
      <button class="button" @click="suspend">Suspend/Unsuspend</button>
    </article> 
  </div>

</template>

<style scoped>
.container {
  margin: 10;
} 

.user-data {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  margin: 0px 90px 10px 90px;
  padding: 8px 0px;
  border: none;
  gap: 2px;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
  box-shadow: 2px 5px 8px 1px rgb(194, 194, 194);
}

.user-data span{
  padding-left: 8px;
}

.header {
  display: flex;
  margin: 10px 90px 0px 90px;
  padding: 8px;
  border-top-right-radius: 8px;
  border-top-left-radius: 8px;
  color: white;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: var(--primary-blue);
}

.suspended {
  background-color: var(--primary-red);
}

.header h4 {
  margin: 3px;
}

.button {
  border: none;
  border-radius: 4px;
  color: white;
  margin: 6px 8px;
  padding: 8px;
  background-color: var(--secondary-red);
}

.button:hover {
  filter: brightness(1.3);
}

.unsuspend {
  background-color: var(--primary-blue);
}
</style>
  




