<script setup>
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    import NavSuite from '../components/NavSuite.vue';
    import GigData from './components/GigData.vue'
    import Heart from '../components/Heart.vue'
    import Popup from '../components/Popup.vue'
    import PinkButton from '../components/PinkButton.vue'

    const gigs = ref([])
    const popupActive = ref(false)
    const activeGig = ref({})
    const message = ref("")
    const heartState = ref([false,false,false,false,false])
    const rating = ref(0)

    const user_id  = parseInt(window.location.hash.split('/')[4]) //Gets the id from the router

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
            'dater_id':activeGig.value.dater_id,
            'gig_id':activeGig.value.id,
            'message':message.value,
            'rating':rating.value
        })
        toggleActiveGig()
    }

    function checkHeart(e) {
        const target = e.target.parentNode
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
    <NavSuite title='Completed Gigs' profile='CupidDetails'>
        <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
        <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
        <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gigs Available </router-link>
        <router-link class="link" :to="{name: 'CupidFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <main>
        <h1>Completed Gigs</h1>
        <div class="gig" v-for="(gig, index) in gigs">
            <GigData :gig="gig"/>
            <PinkButton @click-forward="toggleActiveGig(gig)">Rate Dater</PinkButton>
        </div>
        <Popup :data-active="popupActive">
            <h1>Rate</h1>
            <label class="update-content" for="message">
                <textarea id="message" v-model="message"/>
            </label>
            <label class="update-content" for="rating">
                <div class="row" @click="checkHeart">
                    <Heart v-for="i in 5" :data-index="i - 1" :data-active="heartState[i - 1]"/>
                </div>
            </label>
            <div class="space-evenly">
                <PinkButton @click-forward="sendReview">Send</PinkButton>
                <PinkButton @click-forward="toggleActiveGig">Cancel</PinkButton>
            </div>
        </Popup>
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
        align-content: space-evenly;
    }
    .space-evenly > * {
        margin: 16px;
    }

    .popup h1 {
        margin: auto;
        margin-top: 12px;
        margin-bottom: 4px;
        width: fit-content;
    }

    .popup div {
        margin: auto;
    }
    .row {
        display: flex;
        flex-direction: row;
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
