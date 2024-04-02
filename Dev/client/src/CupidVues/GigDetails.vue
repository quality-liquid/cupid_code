<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    const gigCount = 0
    const gigs = ref([])
    const activeGig = ref({})

    const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router
    // Open and closes drawer w/ shorthand
    function openDrawer() {
        const element = document.getElementById('navbar')
        if (element.className === 'navbar') {
            element.className = 'navbar opened'
        }
        else {
            element.className = 'navbar'
        }
    }
    // Logout function
    async function logout() {
        const result = await makeRequest(`/logout/`)
        router.push('/')
    }

    async function getData() {
        gigs.value = await makeRequest(`api/gig/${user_id}/${gigCount}`)
    }

    function statusConvert(statusNum){
        switch (statusNum) {
            case 0:
                return 'Unclaimed'
            case 1:
                return 'Claimed'
            case 2:
                return 'Complete'
        }
    }

    async function claim(id) {
        activeGig.value = await makeRequest('/api/gig/accept/','post',{
            'gig_id':id
        })
    }

    onMounted(getData)
</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
        </button>
        <!-- This will be the profile picture when setup -->
        <img :src="'/get_menu/'" alt="Profile Picture" class="icon">
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
            <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
            <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}"> Check Completed </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <div class="gig blue" v-if="activeGig.value">
        <h1>Gig Details | Dater: {{ activeGig.dater }}</h1>
        <p>Items requested: {{ activeGig.quest.items_requested }}</p>
        <p>Budget: {{ activeGig.quest.budget }}</p>
        <p>Pickup Location: {{ activeGig.quest.pickup_location }}</p>
        <p>Status: {{ statusConvert(activeGig.status) }}</p>
        <button @click="claim(activeGig.id)">Claim</button>
    </div>
    <ul v-for="(gig, index) in gigs">
        <div class="gig">
            <h1>Gig Details | Dater: {{ gig.dater }}</h1>
            <p>Items requested: {{ gig.quest.items_requested }}</p>
            <p>Budget: {{ gig.quest.budget }}</p>
            <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
            <p>Status: {{ statusConvert(gig.status) }}</p>
            <button @click="claim(gig.id)">Claim</button>
        </div>
    </ul>
</template>

<style scoped>
    .gig {
        background-color: red;
    }
    .blue {
        background-color: blue;
    }
    .show {
        display: block;
    }
    .hidden {
        display: none;
    }
    .active {
      background-color: blue;
    }
    .inactive {
      background-color: red;
    }
</style>
