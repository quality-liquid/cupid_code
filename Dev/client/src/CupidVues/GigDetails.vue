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
            <p>{{ gig }}</p>
            <!-- gig.location is just the City and state -->
            <h1>Gig Details | {{gig.location}}</h1>
            <p>Pickup: gig.pickup</p>

            <!-- If a gig is active, show user info. If not active, don't show user info -->
            <div>
                <img src="" alt=""> <!-- Put picture of dater that submitted the gig here -->
                <label>
                    <input type="checkbox" v-model="pickupComplete"> Pickup Complete
                </label>

                <p>Deliver: gig.deliver </p>
                <p>Address:  gig.address </p>

                <!-- If pickup is complete, show complete gig button -->
                <!-- If complete gig is clicked, reroute to GigComplete Page-->
                <button v-if="pickupComplete" @click="">Complete Gig</button> 
            </div>
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
