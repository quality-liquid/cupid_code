<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

const feedback = ref([])

async function getFeedback() {
    const res = await makeRequest(`/api/cupid/ratings/${user_id}`)
    feedback.value = res
}

onMounted(getFeedback)
</script>

<template>
    <NavSuite title='Feedback' profile='CupidDetails'>
        <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
        <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
        <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gigs Available </router-link>
        <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}"> Gigs Completed </router-link>
    </NavSuite>

    <div class="container">
        <div v-for="item, index of feedback">
            <div :class="index % 2 === 0 ? 'feedback even' : 'feedback odd'">
                <h1>{{ 'Star Rating: ' + item.star_rating }}</h1>
                <span>{{ 'Feedback:\n ' + item.message }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    margin: 40px;
    margin-top: 50px;
}
.feedback {
    padding: 16px;
    border-radius: 16px;
    margin: 10px;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.even {
    background-color: var(--secondary-blue);
}

.odd {
    background-color: var(--secondary-red);
}

.feedback h1 {
    color: white;
}

.even span {
    background-color: var(--primary-blue);
    padding: 6px;
    border-radius: 4px;
}

.odd span {
    background-color: var(--primary-red);
    padding: 6px;
    border-radius: 4px;
}
</style>
