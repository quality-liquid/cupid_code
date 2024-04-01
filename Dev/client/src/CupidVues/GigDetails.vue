<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    const gigCount = 0
    const gigs = ref([])

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
        let gig = await makeRequest('/api/gig/accept/','post',{
            'gig_id':id
        })
        for (let i = 0; i < gigs.lenth; i++){
            console.log(gigs)
            if(gigs[i].id == gig.id){
                gigs[i] = gig
            }
        }
        console.log(gigs)
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

    <h1><br/>You are in GigDetails.vue</h1>
    <!-- If a gig is active, background is blue. If inactive, background is red -->
    <ul v-for="(gig, index) in gigs">
        <div class="gig">
            <!-- gig.location is just the City and state -->
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
