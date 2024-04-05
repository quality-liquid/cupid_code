<script setup>
    import {ref, onMounted} from 'vue';
    import router from '../router/index';
    import { makeRequest } from '../utils/make_request';

    import NavSuite from '../components/NavSuite.vue';

    const user_id  = parseInt(window.location.hash.split('/')[3])

    const balance = ref(0)

    function addFunds(amount) {
        router.push({name: 'AddMoney', params: {id: user_id, amt: amount}})
    }

    async function getMoney() {
        const results = await makeRequest(`/api/dater/balance/${user_id}`)
        balance.value = results.balance
    }

    onMounted(getMoney)   
</script>

<template>  
    <NavSuite title='Add Cash' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <div class="container">
        <h1>Cupid Cash</h1>
        <span>{{'$' + balance}}</span>
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

.container h1 {
    margin-top: 50px;
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
