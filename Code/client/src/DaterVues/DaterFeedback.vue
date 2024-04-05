<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

const user_id  = parseInt(window.location.hash.split('/')[3])

const feedback = ref([])

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

async function getFeedback() {
    const res = await makeRequest(`/api/dater/ratings/${user_id}`) 
    feedback.value = res
}

onMounted(getFeedback)
</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <span class="material-symbols-outlined icon">menu</span>   
        </button>
        <span>Feedback</span>
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
            <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>
    <div class="container">
        <div v-for="item, index of feedback">
            <div :class="index % 2 === 0 ? 'feedback even' : 'feedback odd'">
                <h1>{{ 'Star Rating: ' + item.star_rating }}</h1>
                <span>{{ 'Feedback:\n ' + item.message }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    margin: 40px;
    margin-top: 50px;
}
.feedback {
    padding: 16px;
    border-radius: 16px;
    margin: 10px;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.even {
    background-color: var(--secondary-blue);
}

.odd {
    background-color: var(--secondary-red);
}

.feedback h1 {
    color: white;
}

.even span {
    background-color: var(--primary-blue);
    padding: 6px;
    border-radius: 4px;
}

.odd span {
    background-color: var(--primary-red);
    padding: 6px;
    border-radius: 4px;
}
</style>
