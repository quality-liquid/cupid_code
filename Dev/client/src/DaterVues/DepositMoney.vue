<script setup>
    import { makeRequest } from '../utils/make_request';
    import {ref} from 'vue';

    const user_id  = parseInt(window.location.hash.split('/')[3])
    const amount = parseInt(window.location.hash.split('/')[4])

    const savedCards = ref([])

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

    async function getSaved() {
        const results = await makeRequest()
    }

    async function addFunds() {
        const results = await makeRequest()
    }
</script>

<template>  
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
        </button>
        <!-- This will be the profile picture when setup -->
        <span>Current Balance</span>
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
            <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
            <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
            <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
            <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <div class="container">
        <h1>Payment Information</h1>
        <form class="input-container" @submit.prevent="addFunds">
            <label class="details" for="saved-cards">
                <select name="saved-cards" id="saved-cards" v-for="card of savedCards">
                    <option :value="card">{{ card.name }}</option>
                </select>
            </label>
            <label class="details" for="card-name">  
                <input type="text" name="card-name" id="card-name" placeholder="Name on Card">
            </label>
            <div class="date">
                <label class="details" for="month">  
                    <input type="text" size="5" name="month" id="month" placeholder="MM">
                </label>
                <label class="details" for="year">  
                    <input type="text" size="5" name="year" id="year" placeholder="YY">
                </label>
                <label class="details" for="security-code">  
                    <input type="text" size="5" name="security-code" id="security-code" placeholder="CVV">
                </label>
            </div>
            <label class="details" for="card-type">  
                <input type="text" name="card-type" id="card-type" placeholder="Card Type">
            </label>
            <button class="button">Save</button>
        </form>
    </div>
</template>

<style scoped>

.container {
    display: flex;
    justify-content: center;
    align-content: center;
    margin-top: 40px;
    flex-direction: column;
}


h1 {
    margin: 10px;
    margin-bottom: 15px;
    color: var(--secondary-blue);
}

.details input{
    display: flex;
    margin: 10px;
    border: 1px solid rgb(139, 139, 139);
    gap: 8px;
    border-radius: 4px;
    padding: 16px;
    color: rgb(139, 139, 139);
}

.date {
    display: flex;
    flex-direction: row;
}

.button {
    display: flex;
    justify-content: center;
    align-content: center;
    border: none;
    border-radius: 8px;
    padding: 16px;
    margin: 10px;
    color: white;
    background-color: var(--secondary-red);
}

input:focus {
    border-color: var(--secondary-red);
}

</style>