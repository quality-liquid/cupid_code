<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

const cupids = ref([{ }])
const cupidCount = ref(0)

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

async function getCupids() {
  const res = await makeRequest('/api/manager/cupids/')
  cupids.value = res
  console.log(res[0].user)
}

async function suspend() {

}
  
onMounted(getCupids)
</script>

<template>
  <nav class="nav homenav">
      <button @click="openDrawer" class="icon-button">
          <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
      </button>
      <span>Cupid Information</span>
      <img :src="'/get_person/'" alt="Person" class="icon">
      <div id="navbar" class="navbar">
          <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
          <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
          <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
          <button class="logout" @click="logout"> Logout </button>
      </div>
  </nav>
  <figure>{{ cupidCount }} Cupids</figure>

  <!-- header & button need turnary stuff to swap between suspend/unsuspend -->
  <div v-for="cupid of cupids" class="container">
    <div class="header">
      <img :src="'/get_temp_pfp/'" alt="Profile Picture" class="icon">
      <h4>{{ cupid.user}}</h4>
    </div>
    <article class="user-data">
      <span>Rating: {{ cupid.rating_sum }}</span>
      <span>Location: {{ cupid.location }}</span>
      <span>Completed Gigs: {{ cupid.gigs_completed }}</span>
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