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
        <router-link class="link" :to="{name: 'ManagerHome', params: {id: user_id}}">
          Home 
        </router-link>
        <router-link class="link" :to="{name: 'ManageDaters', params: {id: user_id}}">
          See Dater Info 
        </router-link>
        <router-link class="link" :to="{name: 'ManageCupids', params: {id: user_id}}">
          See Cupid Info 
        </router-link>
    </NavSuite>
  <figure>{{ cupidCount }} Cupids</figure>

  <!-- header & button need turnary stuff to swap between suspend/unsuspend -->
  <div v-for="cupid of cupids" class="container">
    <div class="header" :id="`header-${cupid.user ? cupid.user['id'] : ''}`">
      <span class="material-symbols-outlined icon">person</span>
      <h4>{{ cupid.user ? (cupid.user['first_name'] + " " + cupid.user['last_name']) : ''}}</h4>
      <h4 :id="`id-${cupid.user ? cupid.user['id'] : ''}`">
        {{ cupid.user ? cupid.user['id'] : '' }}
      </h4>
    </div>
    <article class="user-data">
      <span>Rating: {{ cupid.rating_sum }}</span>
      <span>Location: {{ cupid.location }}</span>
      <span>Completed Gigs: {{ cupid.gigs_completed }}</span>
      <button 
        :id="`button-${cupid.user ? cupid.user['id'] : ''}`" 
        class="button" 
        @click="() => suspend(cupid.user ? cupid.user['id'] : '')"
      >
        Suspend
      </button>
    </article> 
  </div>

</template>

<style scoped>
.container {
  margin: 30px 0;
}

.user-data {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  margin: 0 auto 10px auto;
  max-width: 920px;
  padding: 10px 14px;
  border: none;
  gap: 6px;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
  box-shadow: 2px 5px 8px 1px rgb(194, 194, 194);
  background: #fff;
}

.user-data span{
  padding-left: 6px;
}

.header {
  display: flex;
  margin: 10px auto 0 auto;
  max-width: 920px;
  padding: 10px 14px;
  border-top-right-radius: 8px;
  border-top-left-radius: 8px;
  color: white;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: var(--primary);
}

.header .icon { margin-right: 8px; }

.suspended {
  background-color: var(--destructive);
}

.header h4 {
  margin: 3px;
}

.button {
  border: none;
  border-radius: 6px;
  color: var(--accent-foreground);
  margin: 6px 8px;
  padding: 8px 10px;
  background-color: var(--accent);
}

.button:hover {
  filter: brightness(1.05);
}

.unsuspend {
  background-color: var(--primary);
}

@media (max-width: 720px) {
  .header, .user-data { padding: 10px; margin-left: 12px; margin-right: 12px; }
  .button { width: 100%; box-sizing: border-box; margin: 8px 0 0 0; }
  .header { flex-direction: row; gap: 8px; }
}

@media (max-width: 420px) {
  .header h4 { font-size: 0.95rem; }
  .user-data span { font-size: 0.95rem; }
}
</style>
