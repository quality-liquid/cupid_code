<script setup>
    import {ref} from 'vue';
    import router from '../router/index'

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

    function addFunds(amount) {
        
        router.push({name: 'AddMoney', params: {id: user_id, amt: amount}})
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
        <h1>Cupid Cash</h1>
        <div class="money-container">
            <button id="5" class="money-widget" @click="() => addFunds(5)">
                Add 5!!!
            </button>
            <button id="10" class="money-widget" @click="() => addFunds(10)">
                Add 10!!
            </button>
            <button id="30" class="money-widget" @click="() => addFunds(30)">
                Add 30!!
            </button>
            <button id="50" class="money-widget" @click="() => addFunds(50)">
                Add 50!!
            </button>
            <button id="50" class="money-widget" @click="() => addFunds(100)">
                Add 100!
            </button>
        </div>
    </div>
</template>

<style scoped>
.container {
    margin: 40px;
}
.money-container {
    display: flex;
    flex-flow: row wrap;
}

.money-widget {
    background-color: var(--secondary-blue);
    padding: 50px;
    margin: 10px;
    border: none;
    border-radius: 8px;
    text-align: center;
    color: white;
    gap: 10px;
}
</style>