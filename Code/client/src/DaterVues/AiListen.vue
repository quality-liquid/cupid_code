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
let audio = null
let recorder = null

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

    const options = { mimeType: "audio/wav" };
    const recordedChunks = [];
    recorder = new MediaRecorder(stream, options);
    
    recorder.addEventListener("dataavailable", e => {
        if (e.data.size > 0) {
            console.log(e.data)
            recordedChunks.push(e.data);
        }
    });

    recorder.addEventListener("stop", async () => {
        console.log(recordedChunks)
        audio = new Blob(recordedChunks);
        const data = await audio.text()

        const reader = new FileReader()
        reader.readAsDataURL(audio); 
        reader.onloadend = async () => {
            const base64data = reader.result;                
            const result = await makeRequest('/api/stt/', 'post', {
                user: {
                    id: user_id
                },
                audio: {
                    type: audio.type ? audio.type : 'wav',
                    data: base64data 
                }
            })
            console.log(result)
        }
        /*
        const result = await makeRequest('/api/stt/', 'post', {
            user: {
                id: user_id
            },
            audio: {
                type: audio.value.type ? audio.value.type : 'webm',
                data: data 
            }
        })
        if (result.error) {
            const doc = document.getElementById('chatbox')
            const error = document.createElement('div')
            error.setAttribute('class', '')
            error.innerText = result.error
            doc.appendChild(error)
        } else {
            const doc = document.getElementById('chatbox')
            const text = document.createElement('div')
            text.setAttribute('class', '')
            text.innerText = result.data
            doc.appendChild(text)
        }
        */
    });

    recorder.start();
}

async function stopListen() {
    recorder.stop();
    recorder = null;

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
        <div class="text" id="chatbox">
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

.message {
    display: flex;
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
