<script setup>
import {ref} from 'vue'
import { makeRequest } from '../utils/make_request';

import PinkButton from '../components/PinkButton.vue';
import Popup from '../components/Popup.vue';
import NavSuite from '../components/NavSuite.vue';

const audioFile = ref({
    type: '',
    data: ''
})
const audio = ref(null)
const recorder = ref(null)

const popupActive = ref(false)
const budget = ref('')
const items_requested = ref('')
const pickup_location = ref('')

const user_id  = parseInt(window.location.hash.split('/')[3])

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

async function listen() {
    const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false
    });

    const options = { mimeType: "audio/webm" };
    const recordedChunks = [];
    recorder.value = new MediaRecorder(stream, options);

    recorder.value.addEventListener("dataavailable", e => {
        if (e.data.size > 0) {
            recordedChunks.push(e.data);
        }
    });

    recorder.value.addEventListener("stop", async () => {
        audio.value = new Blob(recordedChunks);
        const data = await audio.value.text()
        audioFile.value = {
            type: audio.value.type ? audio.value.type : 'WAV',
            data: data
        }
        const result = await makeRequest('/api/stt/', 'post', {
        audio: audioFile
    })
    });

    recorder.value.start();
}

async function stopListen() {
    recorder.value.stop();
    recorder.value = null;

}

</script>

<template>
    <NavSuite title='Let the AI Listen in!' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <div class="container">
        <div class="buttons">
            <button class="listen button" @click="listen">
                <span class="material-symbols-outlined">mic</span>
            </button>
            <button class="listen button" @click="stopListen">
                <span class="material-symbols-outlined">mic_off</span>
            </button>
            <button class="emergency button" @click="toggleEmergency">
                <span class="material-symbols-outlined">priority_high</span>
            </button>
        </div>
        <Popup :data-active="popupActive">
            <h1>Create Gig</h1>
            <label class="update-content" for="budget">
                Budget
                <input type="text" id="budget" v-model="budget"/>
            </label>
            <label class="update-content" for="items_requested">
                Items Requested
                <input type="text" id="items_requested" v-model="items_requested"/>
            </label>
            <label class="update-content" for="pickup_location">
                Pickup Location
                <input type="text" id="pickup_location" v-model="pickup_location"/>
            </label>
            <div class="space-evenly">
                <PinkButton @click-forward="sendEmergency">Send</PinkButton>
                <PinkButton @click-forward="toggleEmergency">Cancel</PinkButton>
            </div>
        </Popup>
        <div class="text">
            Chatbox
            Add listening functionality here
            <audio> </audio>
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
    box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
}

.button:hover {
    filter: brightness(0.6);
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

.space-evenly {
    display: flex;
    flex-direction: row;
    align-content: space-evenly;
}

.space-evenly > * {
    margin: 16px;
}

.popup h1 {
    margin: auto;
    margin-top: 12px;
    margin-bottom: 4px;
    width: fit-content;
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
