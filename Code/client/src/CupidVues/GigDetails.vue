<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    const gigCount = 0
    const gigs = ref([])
    const activeGigs = ref([])

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
        activeGigs.value = await makeRequest(`api/cupid/gigs/${user_id}/`)
        //Django returns a 404 if there none of either of these. We have to tell Vue it is ok.
        if (gigs.value.detail === 'Not found.'){
            gigs.value = []
        }
        if (activeGigs.value.detail === 'Not found.'){
            activeGigs.value = []
        }
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
        await makeRequest('/api/gig/accept/','post',{
            'gig_id':id
        })
        getData()
    }

    async function complete(id) {
        await makeRequest('/api/gig/complete/','post',{
            'gig_id':id
        })
        getData()
    }


    async function drop(id) {
        await makeRequest('/api/gig/drop/','post',{
            'gig_id':id
        })
        getData()
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

    <main>
        <h1>Active</h1>
        <hr/>
        <ul v-for="(gig, index) in activeGigs">
            <div class="gig active">
                <h1>Dater: {{ gig.dater }}</h1>
                <p>Items requested: {{ gig.quest.items_requested }}</p>
                <p>Budget: ${{ gig.quest.budget }}</p>
                <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
                <div class="space-evenly">
                    <button class="button" @click="complete(gig.id)">Complete</button>
                    <button class="button" @click="drop(gig.id)">Drop</button>
                </div>
            </div>
        </ul>
        <p v-if="activeGigs.length == 0">You are not currently on any gigs.</p>
        <h1>Available</h1>
        <hr/>
        <ul v-for="(gig, index) in gigs">
            <div class="gig inactive">
                <h1>Dater: {{ gig.dater }}</h1>
                <p>Items requested: {{ gig.quest.items_requested }}</p>
                <p>Budget: ${{ gig.quest.budget }}</p>
                <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
                <button class="button" @click="claim(gig.id)">Claim</button>
            </div>
        </ul>
        <p v-if="gigs.length == 0">There are no gigs available.</p>
    </main>
</template>

<style scoped>
    .gig {
        border-radius: 12px;
        padding: 12px;
        color: white;
    }
    .gig h1 {
        margin: 0;
    }
    .space-evenly {
        display: flex;
        flex-direction: row;
        align-contents: space-evenly;
    }
    .active {
        background-color: var(--secondary-red);
        border-color: var(--primary-red);
    }
    .inactive {
        background-color: var(--secondary-blue);
    }
    .button {
        width: auto;
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
        box-shadow: 3px 3px 2px rgba(128, 128, 128, 0.5);
        text-decoration: solid;
        padding: 16px;
        margin: auto;
        display: flex;
        justify-self: center;
        align-self: center;
    }
    hr {
        border: 1px solid #F0F0F0;
        border-radius: 30%;
        margin: 6px;
    }
    main {
        position: absolute;
        top: 42px;
        left: 0px;
        right: 0px;
        padding: 8px;
        display: flex;
        flex-direction: column;
        align-content: center;
    }
    h1,
    p {
        margin: auto;
    }
</style>
