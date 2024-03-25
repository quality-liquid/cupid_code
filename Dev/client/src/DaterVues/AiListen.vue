<script setup>
import {ref} from 'vue'
import { makeRequest } from '../utils/make_request';

const audioFile = ref({
    'type': '',
    'data': ''
})

const quest = ref({
    'budget': 0.0,
    'items_requested': '',
    'pickup_location': ''
})

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

async function sendFile() {
    const result = await makeRequest('/api/stt', 'post', {
        audio: audioFile
    })
}

async function sendEmergency() {
    quest.value = {
        // Get the data from the popup 
    }
    const result = await makeRequest('/api/gig/create', 'post', {
        quest
    })
}

function listen() {

}

function stopListen() {

}

</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
        </button>
        <!-- This will be the profile picture when setup -->
        <img :src="'/get_temp_pfp/'" alt="Profile Picture" class="icon">
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
        <div class="buttons">
            <button class="listen button" @click="listen">
                <img :src="'/get_mic/'" class="icon">
            </button>
            <button class="listen button" @click="stopListen">
                <img :src="'/get_mic_off/'" class="icon">
            </button>
            <button class="emergency button" @click="sendEmergency">
                <img :src="'/get_emergency/'" class="icon">
            </button>
        </div>
        <div class="text">
            Chatbox
            Add listening functionality here
            
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 40px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-content: center;
}

.button {
    display: flex;
    justify-content: center;
    border: none;
    border-radius: 50%;
    height: 50%;
    padding: 30px;
    margin: 2px 4px;
    color: white;
}

.listen {
    background-color: var(--secondary-blue);
}

.emergency {
    background-color: var(--secondary-red);
}

.text {
    display: flex;
    border-top: 4px solid var(--primary-red);
    margin: 10px;
    padding: 10px;
    justify-content: center;
    align-content: center;
    text-align: center;
}
</style>