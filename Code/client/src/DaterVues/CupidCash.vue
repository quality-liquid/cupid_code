<script setup>
    import {ref, onMounted} from 'vue';
    import router from '../router/index';
    import { makeRequest } from '../utils/make_request';

    import NavSuite from '../components/NavSuite.vue';

    const user_id  = parseInt(window.location.hash.split('/')[3])

    const balance = ref(0)
    const cards = ref([])
    const cardIndex = ref(0)
    const amount = ref(0)

    const chosenCard = ref(0)

    const name = ref('')
    const num = ref('')
    const mon = ref('')
    const year = ref('')
    const cvv = ref('')

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
        const card_id = res.id
        const new_res = await makeRequest('/api/dater/transfer/', 'post', {
            user: user_id,
            card_id: card_id,
            amount: amount
        })

        router.push({name: 'CupidCash', params: {id: user_id}})
    }


    async function getMoney() {
        const results = await makeRequest(`/api/dater/balance/${user_id}`)
        balance.value = results.balance
        
        cards.value = await makeRequest(`/api/dater/get_cards/${user_id}`)
        console.log(cards)
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
        <h1>{{ 'Current balance: $' + balance }}</h1>
        <form class="container" @submit.prevent="addFunds">
            <select v-model="cardIndex">
                <option disabled selected>Saved cards</option>
                <option v-for="(card, i) in cards" :value="i">***{{ card.card_number.slice(card.card_number.length-4) }}</option>
            </select>
            <div class="oneline">
                <input type="number" min="0" id="amount" v-model="amount"/>
                <button class="button">Deposit</button>
            </div>
        </form>
        <h1>Add Card</h1>
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
            <button class="button">Save Card</button>
        </form>
    </div>
</template>

<style scoped>
.container h1 {
    margin-top: 50px;
    text-align: center;
}

.container {
    display: flex;
    justify-content: center;
    align-content: center;
    margin-left: 12px;
    margin-right: 12px;
    flex-direction: column;
}

.input-container input {
    border: none;
    box-sizing: border-box;
    outline: 0;
    padding: 12px;
    width: 100%;
}

.oneline {
    display: flex;
    flex-direction: row;
}

select,
.oneline > input{
    margin: auto;
    display: flex;
    border: 1px solid rgb(139, 139, 139);
    gap: 8px;
    border-radius: 4px;
    padding: 16px;
    color: rgb(139, 139, 139);
    width: 100%;
}

select {
    color: black;
}

.details input{
    display: flex;
    margin: 4px;
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
