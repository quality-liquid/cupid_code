<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';
import NavSuite from '../components/NavSuite.vue';

const cupids = ref([{ }])
const cupidCount = ref(0)

const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router

async function getCupids() {
  const res = await makeRequest('/api/manager/cupids/')
  cupids.value = res
}

async function suspend(id) {
  const header = document.getElementById(`header-${id}`)
  const button = document.getElementById(`button-${id}`)
  
  if (header.attributes.class.value.includes('suspended')) {
    header.setAttribute('class', 'header')
    button.innerText = 'Suspend'
    const res = await makeRequest('/api/manager/unsuspend/', 'post', {
      user_id: id,
      role: 'Cupid'
    })
  }
  else {
    header.setAttribute('class', 'header suspended')
    button.innerText = 'Unsuspend'
    const res = await makeRequest('/api/manager/suspend/', 'post', {
      user_id: id,
      role: 'Cupid'
    })
  }
}
  
onMounted(getCupids)
</script>

<template>
    <NavSuite title='Cupid Information'>
        <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}"> Home </router-link>
        <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}"> See Dater Info </router-link>
        <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}"> See Cupid Info </router-link>
    </NavSuite>
  <figure>{{ cupidCount }} Cupids</figure>

  <!-- header & button need turnary stuff to swap between suspend/unsuspend -->
  <div v-for="cupid of cupids" class="container">
    <div class="header" :id="`header-${cupid.user ? cupid.user['id'] : ''}`">
      <span class="material-symbols-outlined icon">person</span>
      <h4>{{ cupid.user ? (cupid.user['first_name'] + " " + cupid.user['last_name']) : ''}}</h4>
      <h4 :id="`id-${cupid.user ? cupid.user['id'] : ''}`">{{ cupid.user ? cupid.user['id'] : '' }}</h4>
    </div>
    <article class="user-data">
      <span>Rating: {{ cupid.rating_sum }}</span>
      <span>Location: {{ cupid.location }}</span>
      <span>Completed Gigs: {{ cupid.gigs_completed }}</span>
      <button :id="`button-${cupid.user ? cupid.user['id'] : ''}`" class="button" @click="() => suspend(cupid.user ? cupid.user['id'] : '')">Suspend</button>
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
