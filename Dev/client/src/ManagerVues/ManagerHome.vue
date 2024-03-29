<script setup>
// NOTE: I tried matching the results names to what I can see in the views.py and helper.py 
//If things are reading null or undefined, just console.log(results) to see what the names are and then change `results.data` to `results.<foundName>`
import {ref, onMounted} from 'vue'
import { makeRequest } from '../utils/make_request';

const daters = ref(0) //Fill with a setter type for whatever the backend returns to you 
const cupids = ref(0)
const active_cupids = ref(0)
const active_daters = ref(0)

async function getDatersTotal() {
  const results = await makeRequest('/api/manager/dater_count/')
  daters.value = results.count
}

async function getCupidsTotal() {
  const results = await makeRequest('/api/manager/cupid_count/')
  cupids.value = results.count
}

async function getCurrActiveTotal() {
  const cupid_res = await makeRequest('/api/manager/active_cupids/')
  active_cupids.value = cupid_res.data 
  const dater_res= await makeRequest('/api/manager/active_daters/')
  active_daters.value = dater_res.data
}

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

onMounted(() => {
  getCupidsTotal()
  getDatersTotal()
  getCurrActiveTotal()
})
</script>

<template>
  <nav class="nav homenav">
      <button @click="openDrawer" class="icon-button">
          <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
      </button>
      <span>Home</span>
      <!-- This will be the profile picture when setup -->
      <img :src="'/get_temp_pfp/'" alt="Profile Picture" class="icon">
      <div id="navbar" class="navbar">
          <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
          <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
          <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
          <button class="logout" @click="logout"> Logout </button>
      </div>
  </nav>
  <main class="container">
    <div class="widget-container">
      <div class="widget blue">
        <img :src="'/get_person/'" alt="Menu Open icon" class="wid_icon">
        <router-link class="header" :to="{name: 'ManageCupids', params: {id: user_id}}">Cupids</router-link>
      </div>
      <div class="widget red"> <!-- This will become Calendar when it's made -->
        <img :src="'/get_heart/'" alt="Menu Open icon" class="wid_icon">
        <router-link class="header" :to="{name: 'ManageDaters', params: {id: user_id}}">Daters</router-link>
      </div>
    </div>
    <h3>Revenue Graph (Very Real)</h3>
    <figure class="graph-container">
      <img :src="'/get_graph/'" alt="Graph" class="graph" width="300px">
      <figcaption>Graph of Overall Revenue</figcaption>
    </figure>
  
    <h3>General Stats</h3>
    <div class="stat-container">
      <div class="stat-widget">
        <h4 class="stat">{{ daters }}</h4> 
        <span>Total Daters</span>
      </div>
      <div class="stat-widget">
        <h4 class="stat">{{ cupids }}</h4>
        <span>Total Cupids</span>
      </div>
      <div class="stat-widget">
        <h4 class="stat">{{ active_cupids || 0}}</h4> 
        <span>Active Cupids</span>
      </div>
      <div class="stat-widget">
        <h4 class="stat">{{ active_daters || 0 }}</h4>
        <span>Active Daters</span>
      </div>
    </div>
  </main>

</template>

<style scoped>
.container {
  margin: 10px;
  margin-top: 50px;
}

h3 {
  margin: 4px;
  text-align: center;
}

.graph-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.stat-container {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.stat-widget {
  border: 2px solid var(--primary-blue);
  border-radius: 4px;
  padding: 16px;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  color: grey;
}

.stat {
  color: black;
  margin: 0;

}

.widget-container {
  margin: 10px;
  margin-top: 50px;
  display: flex;
  flex-flow: row wrap;
  justify-content: space-evenly;
  gap: 10px;
}

.widget {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: center;
  padding: 50px;
  border: none;
  border-radius: 16px;
}

.header {
  color: white;
}

.blue {
  background-color: var(--primary-blue);
}

.red {
  background-color: var(--primary-red);
}
</style>
  




