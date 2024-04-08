<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';

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
  
async function suspend(id) {
  const header = document.getElementById(`header-${id}`)
  const button = document.getElementById(`button-${id}`)
  
  if (header.attributes.class.value.includes('suspended')) {
    header.setAttribute('class', 'header')
    button.innerText = 'Suspend'
    const res = await makeRequest('/api/manager/unsuspend/', 'post', {
      user_id: id,
      role: 'Dater'
    })
  }
  else {
    header.setAttribute('class', 'header suspended')
    button.innerText = 'Unsuspend'
    const res = await makeRequest('/api/manager/suspend/', 'post', {
      user_id: id,
      role: 'Dater'
    })
  }
}

onMounted(getDaters)
</script>

<template>
  <!-- nav banner component -->
  <!-- end nav bar -->
  <NavSuite title='Dater Information'>
      <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
      <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
      <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
  </NavSuite>
  <figure>{{ daterCount }} Daters</figure>

  <!-- h4 id needs to relate the suspended/unsuspended user's ID -->
  <div v-for="dater of daters" class="container">
    <div class="header" :id="`header-${dater.user ? dater.user['id'] : ''}`">
      <span class="material-symbols-outlined icon">person</span>
      <h4>{{ dater.user ? (dater.user['first_name'] + " " + dater.user['last_name']) : ''}}</h4>
      <h4 :id="`id-${dater.user ? dater.user['id'] : ''}`">{{ dater.user ? dater.user['id'] : '' }}</h4>
    </div>
    <article class="user-data">
      <span>Rating: {{ dater.rating_sum }}</span>
      <span>Location: {{ dater.location }}</span>
      <button :id="`button-${dater.user ? dater.user['id'] : ''}`" class="button" @click="() => suspend(dater.user ? dater.user['id'] : '')">Suspend</button>
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
  




