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



onMounted(() => getCalendar())
</script>

<template>  
    <nav class="nav homenav">
      <button @click="openDrawer" class="icon-button">
            <span class="material-symbols-outlined icon">menu</span>   
        </button>
      <!-- This will be the profile picture when setup -->
      <button class="icon-button" @click="naviProf">
          <span class="material-symbols-outlined icon">account_circle</span>
      </button>
      <div id="navbar" class="navbar">
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
        <button class="logout" @click="logout"> Logout </button>
      </div>
    </nav>  

    <div class="container">
      <h1>Schedule your next date!</h1>
      <span class="datepicker-toggle">
        <span class="datepicker-toggle-button"></span>
        <input type="date" class="datepicker-input">
      </span>
    </div>
</template>

<style scoped>
.container {
    margin: 40px;
}
.container h1 {
    margin-top: 50px;
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

/* date input css */
/* .datepicker-toggle {
  display: inline-block;
  position: relative;
  width: 18px;
  height: 19px;
}
.datepicker-toggle-button {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-image: url('data:image/svg+xml;base64,...');
} */



/*  */
/* .input-container input {
    border: none;
    box-sizing: border-box;
    outline: 0;
    padding: .75rem;
    position: relative;
    width: 100%;
}
input[type="date"]::-webkit-calendar-picker-indicator {
    background: transparent;
    bottom: 0;
    color: transparent;
    cursor: pointer;
    height: auto;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    width: auto;
} */
</style>