<script setup>
import router from './router/index.js';

const currPath = window.location.hash

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
</script>


<template>
    <div id="app">
      <nav class="nav homenav" v-if="currPath.includes('dater')">
        <button @click="openDrawer" class="icon-button">
                <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
        </button>
        <h3>Hello</h3>
        <div id="navbar" class="navbar">
          <router-link class="link" to="/dater/home"> Home </router-link>
          <router-link class="link" to="/dater/profile/"> Profile </router-link>
          <router-link class="link" to="/dater/chat/"> AI Chat </router-link>
          <router-link class="link" to="/dater/listen/"> AI Listen </router-link>
          <router-link class="link" to="/dater/balance/"> Balance</router-link>
          <a @click="logout"> Logout </a>
        </div>
      </nav>
      <nav class="nav homenav" v-else-if="currPath.includes('cupid')">
        <button @click="openDrawer" class="icon-button">
                <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
        </button>
        <h3>Hello</h3>
        <div id="navbar" class="navbar">
          <router-link class="link" to="/cupid/home"> Home </router-link>
          <a class="link" @click="logout"> Logout </a>
        </div>
      </nav>
      <nav class="nav homenav" v-else-if="currPath.includes('manager')">
        <button @click="openDrawer" class="icon-button">
                <img :src="'/get_icon/'" alt="Menu Open icon" class="icon">
        </button>
        <h3>Hello</h3>
        <div id="navbar" class="navbar">
          <router-link class="link" to="/manager/home"> Home </router-link>
          <a class="link" @click="logout"> Logout </a>
        </div>
      </nav>
      <nav class="nav" v-else>
          <router-link class="link" to="/login"> Login </router-link>
          <router-link class="link" to="/register"> Sign Up </router-link>
          <router-link class="link" to="/"> Welcome </router-link>
      </nav>
    </div>
    <router-view />
</template>

<style scoped>
  .link {
    color: white;
    gap: 10px;
  }
</style>