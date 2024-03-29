<script setup>
import { makeRequest } from '../utils/make_request';
import {onMounted, ref, watch} from 'vue';



const user_id  = parseInt(window.location.hash.split('/')[3])

function openDrawer() {
  const element = document.getElementById('navbar')
  if (element.className === 'navbar') {
    element.className = 'navbar opened'
  }
  else {
    element.className = 'navbar'
  }
}

async function logout() {
  const result = await makeRequest(`/logout/`)
  router.push('/')
}

async function getCalendar() {
  const results = await makeRequest(`/api/dater/calendar/${user_id}`);
  // put calendar to screen

}

// calendar stuffs
const selectedColor = ref('blue');
const attrs = ref([
  {
    key: 'test',
    highlight: true,
    dates: { start: new Date(2019, 3, 15), end: new Date(2019, 3, 19) },
  }
]);
// end calendar stuffs




onMounted(() => getChats())
</script>






<template>  
    <nav class="nav homenav">
      <button @click="openDrawer" class="icon-button">
          <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
      </button>
      <!-- This will be the profile picture when setup -->
      <img :src="'/get_menu/'" alt="Profile Picture" class="icon">
      <div id="navbar" class="navbar">
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <button class="logout" @click="logout"> Logout </button>
      </div>
    </nav>  

    <h2>Calendar</h2>
    <div class="calendar"> 
      <VCalendar borderless expanded title-position="left"
        :color="blue"
        :attributes="attrs"
      />
      <VDatePicker v-model="date" />
    </div>
</template>










<style scoped>
.chatbox {
    display: flex;
    flex-flow: column nowrap;
    margin: 10px;
    margin-top: 40px;
    height: 450px;
    overflow-y: scroll;
}

.chat {
    padding: 8px;
    margin: 8px;
    border: none;
    border-radius: 4px;
}

.sent {
    display: flex;
    justify-content: flex-end;
    background-color: var(--primary-red);
    color: white;
    position: relative;
    margin-bottom: 10px;
    margin-left: calc(100% - 240px);
    padding: 10px;
}

.response {
    display: flex;
    justify-content: flex-start;
    background-color: var(--secondary-blue);
    color: white;
    position: relative;
    margin-bottom: 10px;
    margin-right: calc(100% - 240px);
    padding: 10px;
}

.textbox {
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
    background-color: var(--secondary-red);
    padding: 24px;
}

.message {
    text-align: center;
    color: white;
    display: flex;
    flex-direction: column;
}

.message h4 {
    margin: 4px;
    margin-top: 0px;
}

.message input {
    border: none;
    border-radius: 4px;
    padding: 8px;
    margin: 4px;
}

</style>