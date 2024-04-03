<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    import GigData from './GigData.vue'
    import Heart from './Heart.vue'

    const gigs = ref([])
    const popupActive = ref(false)
    const activeGig = ref({})
    const message = ref("")
    const heartState = ref([false,false,false,false,false])
    const rating = ref(0)

    const user_id  = parseInt(window.location.hash.split('/')[4]) //Gets the id from the router
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

    function naviProf() {
        router.push({ name: 'CupidDetails', params: {id: user_id} })
    }

    async function getData() {
        gigs.value = await makeRequest(`api/cupid/gigs/${user_id}?complete=true`)
        //Django returns a 404 if there are none. We have to tell Vue it is ok.
        if (gigs.value.detail === 'Not found.'){
            gigs.value = []
        }
    }

    function toggleActiveGig(gig) {
        if(popupActive.value){
            popupActive.value = false
            activeGig.value = {}
        }
        else{
            popupActive.value = true
            activeGig.value = gig
        }
    }

    function sendReview() {
        makeRequest('api/dater/rate/', 'post', {
            'dater_id':activeGig.value.dater,
            'gig_id':activeGig.value.id,
            'message':message.value,
            'rating':rating.value
        })
        toggleActiveGig()
    }

    function checkHeart(e) {
        const target = e.target.parentNode.parentNode
        rating.value = Number(target.dataset.index) + 1
        for (let i = 0; i <= rating.value; i++){
            heartState.value[i] = true
        }
        for (let i = rating.value; i < 5; i++){
            heartState.value[i] = false
        }
    }

    onMounted(getData)

</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <span class="material-symbols-outlined icon">menu</span>
        </button>
        <!-- This will be the profile picture when setup -->
        <button class="icon-button" @click="naviProf">
            <span class="material-symbols-outlined icon">account_circle</span>
        </button>
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
            <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
            <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gig Details </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <main>
        <h1>Completed Gigs</h1>
        <div class="gig" v-for="(gig, index) in gigs">
            <GigData :gig="gig"/>
            <div class="space-evenly">
                <button class="button" @click="toggleActiveGig(gig)">Rate Dater</button>
            </div>
        </div>
        <div class="popup" :class="{ active: popupActive }">
            <h1>Rate</h1>
            <label class="update-content" for="message">
                <textarea id="message" v-model="message"/>
            </label>
            <label class="update-content" for="rating">
                <div class="row" @click="checkHeart">
                    <Heart v-for="i in 5" :data-index="i - 1" :data-active="heartState[i - 1]"/>
                </div>
            </label>
            <div>
                <button @click="sendReview">Send</button>
                <button @click="toggleActiveGig">Cancel</button>
            </div>
        </div>
    </main>
</template>

<style scoped>
    .gig {
        border-radius: 12px;
        padding: 12px;
        color: black;
        background-color: var(--content-background);
        border-color: var(--primary-red);
        margin: 6px;
    }
    .gig h1 {
        margin: 0;
    }
    .space-evenly {
        display: flex;
        flex-direction: row;
        align-contents: space-evenly;
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
    .popup {
        position: absolute;
        width: 60%;
        height: 40%;
        margin: auto;
        left:0;
        right:0;
        top: 0;
        bottom: 0;

        transform: scale(0);
        transition: transform 0.2s cubic-bezier(0,1,1,1);

        display: flex;
        flex-direction: column;
        align-content: flex-end;
        background-color: var(--secondary-blue);
        border: 3px solid var(--primary-red);
        color: white;

    }

    .popup label {
        display: flex;
        justify-content: center;
        margin-bottom: 24px;
    }

    .popup input {
        margin-left: 6px;
    }

    .popup h1 {
        margin: auto;
        margin-top: 12px;
        margin-bottom: 4px;
        width: fit-content;
    }

    .popup button {
        margin-left: 3px;
        margin-right: 3px;
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
        box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
        text-decoration: solid;
        padding: 16px;
        margin: 10px;
        user-select: none;
    }

    .popup button:hover {
        filter: brightness(0.9);
    }

    .popup button:active {
        filter: brightness(0.7);
        transform: translate(3px,3px);
        box-shadow: 3px 3px 1px rgba(0, 0, 0, 0.4);
    }

    .popup div {
        margin: auto;
    }

    .row {
        display: flex;
        flex-direction: row;
    }

    .active {
        transform: scale(1);
        transition: transform 0.2s cubic-bezier(0,1.4,1,1);
    }

    .update-content {
        text-align: center;
        margin-bottom: 4px;
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .update-content input{
        border: none;
        border-radius: 4px;
        padding: 8px;
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
</style>
