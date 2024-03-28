<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'
import { makeRequest } from '../utils/make_request';

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

function naviProf() {
  router.push({ name: 'DaterProfile', params: {id: user_id} })
}

async function logout() {
  const result = await makeRequest(`/logout/`)
  router.push('/')
}

</script>

<template>
<nav class="nav homenav">
  <button @click="openDrawer" class="icon-button">
    <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
  </button>
  <!-- This will be the profile picture when setup & will be functioning button -->
  <button class="icon-button" @click="naviProf">
    <img :src="'/get_temp_pfp/'" alt="Profile Picture" class="icon">
  </button>
  <div id="navbar" class="navbar">
    <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
    <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
    <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
    <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
    <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
    <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    <button class="logout" @click="logout"> Logout </button>
  </div>
</nav>  

<div class="container">
  <div class="widget blue">
    <img :src="'/get_chat/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" :to="{name: 'AiChat', params: {id: user_id}}">AI Chat</router-link>
  </div>
  <div class="widget red">
    <img :src="'/get_mic/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" :to="{name: 'AiListen', params: {id: user_id}}">AI Listen</router-link>
  </div>
  <div class="widget blue">
    <img :src="'/get_money/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" :to="{name: 'CupidCash', params: {id: user_id}}">Add Cash</router-link>
  </div>
  <div class="widget red"> <!-- This will become Calendar when it's made -->
    <img :src="'/get_temp_pfp/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" :to="{name: 'DaterProfile', params: {id: user_id}}">Edit Profile</router-link>
  </div>
</div>
</template>

<style scoped>
  .container {
    margin: 10px;
    margin-top: 50px;
    display: flex;
    flex-flow: row wrap;
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
    background-color: var(--secondary-blue);
  }

  .red {
    background-color: var(--secondary-red);
  }
</style>