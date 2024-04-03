<script setup>
    import { makeRequest } from '../utils/make_request';
    import {onMounted, ref} from 'vue';
    import router from '../router';

    const user_id  = parseInt(window.location.hash.split('/')[3])
    const amount = parseInt(window.location.hash.split('/')[4])

    //const savedCards = ref([])

    const balance = ref(0)

    const chosenCard = ref(0)

    const name = ref('')
    const num = ref('')
    const mon = ref('')
    const year = ref('')
    const cvv = ref('')

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

    async function getMoney() {
        const results = await makeRequest(`/api/dater/balance/${user_id}`)
        balance.value = results.balance
    }

    async function addFunds() {
        const res = await makeRequest('/api/dater/transfer/', 'post', {
            user: user_id,
            card_id: chosenCard.value,
            amount: amount
        })
    }

    async function saveCard() {
        // Save card to db
        const exp = `${mon.value}/${year.value}`

        const res = await makeRequest('/api/dater/save_card/', 'post', {
            user: {
                id: user_id
            },
            name_on_card: name.value,
            card_number: num.value,
            cvv: cvv.value,
            expiration: exp
        })
        console.log(res)
        const card_id = res.id
        console.log(amount)
        const new_res = await makeRequest('/api/dater/transfer/', 'post', {
            user: user_id,
            card_id: card_id,
            amount: amount
        })

        console.log(new_res)

        router.push({name: 'CupidCash', params: {id: user_id}})
    }

    onMounted(getMoney)

</script>

<template>  
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <span class="material-symbols-outlined icon">menu</span>   
        </button>
        <span>Add Cash</span>
        <span>{{ '$' + balance }}</span>
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
            <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
            <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
            <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
            <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
            <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
            <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <div class="container">
        <h1>Payment Information</h1>
        <!-- Currently no function to support this
        <div class="saved-container" v-if="savedCards">
            <select v-for="card of saveCards" class="select">
                <option :value={card}>{{ `Card Ending in ${card.card_number.split(" ")[3]}` }}</option>
            </select>
            <button class="button" @click="addFunds">Add Funds</button>
        </div>
        -->
        <form class="input-container" @submit.prevent="saveCard">
            <label class="details" for="card-name">  
                <input type="text" name="card-name" id="card-name" placeholder="Name on Card"
                :value="name" @change="e => name = e.target.value"
                >
            </label>
            <label class="details" for="card-num">  
                <input type="text" name="card-num" id="card-num" placeholder="0000 0000 0000 0000"
                :value="num" @change="e => num = e.target.value"
                >
            </label>
            <div class="date">
                <label class="details" for="month">  
                    <input type="text" size="5" name="month" id="month" placeholder="MM"
                    :value="mon" @change="e => mon = e.target.value"
                    >
                </label>
                <label class="details" for="year">  
                    <input type="text" size="5" name="year" id="year" placeholder="YY"
                    :value="year" @change="e => year = e.target.value"
                    >
                </label>
                <label class="details" for="security-code">  
                    <input type="text" size="5" name="security-code" id="security-code" placeholder="CVV"
                    :value="cvv" @change="e => cvv = e.target.value">
                </label>
            </div>
            <button class="button">Add Funds</button>
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
