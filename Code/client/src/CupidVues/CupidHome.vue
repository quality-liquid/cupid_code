<script setup>
    import { ref, onMounted } from 'vue';
    import { makeRequest } from '../utils/make_request';
    
    const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router
    let gigs = ref('');
    const gigCount = 10;
    
    // Get gigs function
    async function getGigs() {
        gigs.value = await makeRequest(`api/gig/${user_id}/${gigCount}`)
        console.log(gigs.value);
        gigs.value.forEach(element => {
            console.log(element.id)
        });
    }
    
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
    
    onMounted(getGigs);
</script>

<template>
    <NavSuite title='Home' profile='CupidDetails'>
        <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
        <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
        <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gig Details </router-link>
        <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}"> Check Completed </router-link>
    </NavSuite>

    <div class="body">
        <h1><br/>You are in CupidHome.vue</h1>
        <!-- Clicking on this gig item, reroute to GigDetails page -->
        <div v-for="gig of gigs" :key="gig.id">
            <h1>YEET!!!!!!!!!!!!!</h1>
            <div :class="{ 'active': gig.status, 'inactive': !gig.status }" >
                <router-link class="link" :to="{name: 'GigDetails', params: {id: gig.id}}">{{ gig.quest.pickup_location }}</router-link>
            </div>
            
            <p>Pickup: {{ gig.quest.items_requested }}</p>
            <p>Status: {{ gig.status ? 'Active' : 'Inactive' }}</p>
            <button :class="{'active': !gig.status, 'inactive': gig.status}" @click="gig.status ? dropgig(gig.id) : acceptgig(gig.id)">
                {{ gig.status ? 'Drop Gig' : 'Accept' }}
            </button>
        </div>
    </div>

</template>

<style scoped>
    .active {
      background-color: var(--secondary-blue);
    }
    .inactive {
      background-color: var(--secondary-red);
    }
</style>
