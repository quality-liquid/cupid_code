<script setup>
import { makeRequest } from '../utils/make_request';
import {ref} from 'vue';

const chatArr = ref([])
const message = ref('')

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

async function getChats() {
    const results = await makeRequest(`/api/chat/${user_id}`);
    // May need to split results chat to fit into array
    chatArr.value = results.chat
}

async function getResponse() {
    const results = await makeRequest();
    // Put response on screen
}
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

    <div class="chatbox">
        <div class="chat response">Example Chat for Styling Purposes</div> 
        <div class="chat sent">Example Chat for Styling Purposes</div> 
    </div>
    <div class="textbox">
        <label for="message" class="message">
            <h4>Enter Message Here</h4>
            <input id="message" placeholder="Type your message to the AI!" :value="message" @change="(e) =>  message = e.target.value">
        </label>
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