<script setup>
// NOTE: I tried matching the results names to what I can see in the views.py and helper.py 
//If things are reading null or undefined, just console.log(results) to see what the names are and then change `results.data` to `results.<foundName>`
import {ref, onMounted} from 'vue'
import { makeRequest } from '../utils/make_request';
import {to_pdf} from '../utils/to_PDF';
import NavSuite from '../components/NavSuite.vue';

const daters = ref(0) //Fill with a setter type for whatever the backend returns to you 
const cupids = ref(0)
const active_cupids = ref(0)
const active_daters = ref(0)

const gigs = ref(0)
const rate = ref(0)
const dropped = ref(0)
const completed = ref(0)

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

async function getGigData() {
 const rate_res = await makeRequest('/api/manager/gig_rate/')
 const count_res = await makeRequest('/api/manager/gig_count/')
 gigs.value = count_res.count
 const completed_res = await makeRequest('/api/manager/gig_complete_rate/')
 const dropped_res = await makeRequest('/api/manager/gig_drop_rate/')
}

function toPDF() {
  const content = document.querySelector('#content')
  to_pdf(content)
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

onMounted(() => {
  //getCupidsTotal()
  //getDatersTotal()
  //getCurrActiveTotal()
  //getGigData()
})
</script>

<template>
    <NavSuite title='Home'>
          <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
          <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
          <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
    </NavSuite>
  <main class="container">
      <div class="widget-container">
        <div class="widget blue">
          <span class="material-symbols-outlined icon">person</span>
          <router-link class="header" :to="{name: 'ManageCupids', params: {id: user_id}}">Cupids</router-link>
        </div>
        <div class="widget red"> 
          <span class="material-symbols-outlined icon">favorite</span>
          <router-link class="header" :to="{name: 'ManageDaters', params: {id: user_id}}">Daters</router-link>
        </div>
      </div>

    <div id="content">
      <h3>Revenue Graph (Very Real)</h3>
      <figure class="graph-container" name="toPDF">
        <img :src="'/get_graph/'" alt="Graph" class="graph" width="300px">
        <figcaption>Graph of Overall Revenue</figcaption>
      </figure>
      <h3>General Stats</h3>
      <div class="stat-container" name="toPDF">
        <div class="stat-widget">
          <h4 class="stat">250k</h4> 
          <span>Total Daters</span>
        </div>
        <div class="stat-widget">
          <h4 class="stat">60k</h4>
          <span>Total Cupids</span>
        </div>
        <div class="stat-widget">
          <h4 class="stat">40k</h4> 
          <span>Active Cupids</span>
        </div>
        <div class="stat-widget">
          <h4 class="stat">15k</h4>
          <span>Active Daters</span>
        </div>
      </div>
      <h3>Gig Stats</h3>
      <div class="stat-container" name="toPDF">
        <div class="stat-widget gigs">
          <h4 class="stat">500k</h4>
          <span>Total Gigs</span>
        </div>
        <div class="stat-widget gigs">
          <h4 class="stat">40k</h4>
          <span>Gigs per Day</span>
        </div>
        <div class="stat-widget gigs">
          <h4 class="stat">400k</h4>
          <span>Gigs Completed</span>
        </div>
        <div class="stat-widget gigs">
          <h4 class="stat">100k</h4>
          <span>Gigs Dropped</span>
        </div>
      </div>
    </div>
    <button @click="toPDF" class="button">Convert to PDF</button>
    </main>

</template>

<style scoped>
.container {
  margin: 10px;
  margin-top: 50px;
  display: flex;
  flex-flow: column;
  justify-content: center;
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

.button {
  margin: 10px 250px;
  border: none;
  border-radius: 8px;
  background-color: var(--primary-blue);
  color: white;
  padding: 16px;
}
</style>
  




