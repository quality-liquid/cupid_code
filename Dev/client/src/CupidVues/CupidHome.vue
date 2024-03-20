<script setup>
    import { onMounted } from 'vue';
    import { makeRequest } from '../utils/make_request';
    let Gigs = [];
    const numOfGigs = 10;

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

    // Get gigs function
    async function getGigs() {
        const results = await makeRequest(`/api/cupid/getgigs/${numOfGigs}`); 
        Gigs = results.gigs; 
    }
    onMounted(getGigs());

    // Accept gig function 
    async function acceptgig(gigId) {
        await makeRequest(`/api/gig/accept/`, 'post', {
            id: gigId
        });
    }

    // Drop gig function
    async function dropgig(gigId) {
        await makeRequest(`/api/gig/drop/`, 'post', {
            id: gigId
        })
    }

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
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <div class="body">
        <!-- Clicking on this gig item, reroute to GigDetails page -->
        <div v-for="gig in Gigs" :key="gig.id">
            <div :class="{ 'active': gig.status, 'inactive': !gig.status }" >
                <router-link class="link" :to="{name: 'GigDetails', params: {id: gig.id}}">{{ gig.quest.pickup_location }}</router-link>
            </div>
            
            <p>Pickup: {{ gig.quest.items_requested }}</p>
            <p>Status: {{ gig.status ? 'Active' : 'Inactive' }}</p>
            <button :class="{'active': !gig.status, 'inactive': gig.status}" @click="{{ gig.status ? dropgig(gig.id) : acceptgig(gig.id) }}">
                {{ gig.status ? 'Drop Gig' : 'Accept' }}
            </button>
        </div>
    </div>

</template>

<style scoped>
    .active {
      background-color: blue;
    }
    .inactive {
      background-color: red;
    }
</style>