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

const popupActive = ref(false)
const budget = ref('')
const items_requested = ref('')
const pickup_location = ref('')

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

function naviProf() {
    router.push({ name: 'DaterProfile', params: {id: user_id} })
}

async function sendFile() {
    const result = await makeRequest('/api/stt', 'post', {
        audio: audioFile
    })
}

function toggleEmergency() {
    popupActive.value = !popupActive.value;
}

async function sendEmergency() {
    const result = await makeRequest('/api/gig/create/', 'post', {
        "budget":budget._value,
        "items_requested":items_requested._value,
        "pickup_location":pickup_location._value
    })
    popupActive.value = false
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
        <div class="buttons">
            <button class="listen button" @click="listen">
                <img :src="'/get_mic/'" class="icon">
            </button>
            <button class="listen button" @click="stopListen">
                <img :src="'/get_mic_off/'" class="icon">
            </button>
            <button class="emergency button" @click="toggleEmergency">
                <img :src="'/get_emergency/'" class="icon">
            </button>
        </div>
        <div class="popup" :class="{ active: popupActive }">
            <h1>Create Gig</h1>
            <label class="update-content" for="budget">
                Budget
                <input type="text" id="budget" :value="budget" @change="(e) => budget = e.target.value"/>
            </label>
            <label class="update-content" for="items_requested">
                Items Requested
                <input type="text" id="items_requested" :value="items_requested" @change="(e) => items_requested = e.target.value"/>
            </label>
            <label class="update-content" for="pickup_location">
                Pickup Location
                <input type="text" id="pickup_location" :value="pickup_location" @change="(e) => pickup_location = e.target.value"/>
            </label>
            <div>
                <button @click="sendEmergency">Send</button>
                <button @click="toggleEmergency">Cancel</button>
            </div>
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

.popup {
    position: absolute;
    width: 60%;
    height: 40%;
    margin:auto;
    left:0;
    right:0;
    top: 0;
    bottom: 0;

    transform: scale(0);
    transition: transform 0.2s cubic-bezier(0,1,1,1);

    display: flex;
    flex-direction: column;
    align-content: flex-end;
    background-color: var(--secondary-blue);
    border: 3px solid var(--primary-red);
    color: white;

}

.popup label {
    display: flex;
    justify-content: center;
    margin-bottom: 24px;
}

.popup input {
    margin-left: 6px;
}

.popup h1 {
    margin: auto;
    margin-top: 12px;
    margin-bottom: 4px;
    width: fit-content;
}

.popup button {
    margin-left: 3px;
    margin-right: 3px;
    background-color: var(--primary-red);
    border-radius: 10px;
    color: white;
    border: none;
    border-radius: 4px;
    box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
    text-decoration: solid;
    padding: 16px;
    margin: 10px;
}

.popup button:hover {
    filter: brightness(0.9);
}

.popup button:active {
    filter: brightness(0.7);
    box-shadow: 3px 3px 1px rgba(0, 0, 0, 0.4);
}

.popup div {
    margin: auto;
}

.active {
    transform: scale(1);
    transition: transform 0.2s cubic-bezier(0,1.4,1,1);
}

.update-content {
    text-align: center;
    margin-bottom: 4px;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.update-content input{
    border: none;
    border-radius: 4px;
    padding: 8px;
}
</style>
