<script setup>
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    import NavSuite from '../components/NavSuite.vue';
    import GigData from './components/GigData.vue'
    import Heart from '../components/Heart.vue'
    import PinkButton from '../components/PinkButton.vue'

    // Gig lists
    const claimedGigs = ref([])
    const unclaimedGigs = ref([])
    const completeGigs = ref([])

    //Review popup
    const popupActive = ref(false)
    const activeGig = ref({})
    const message = ref("")
    const heartState = ref([false,false,false,false,false])
    const rating = ref(0)


    const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router

    async function getData() {
        const gigs = await makeRequest(`api/dater/gigs/${user_id}`)
        //Django returns a 404 if there none of either of these. We have to tell Vue it is ok.
        if (gigs.detail === 'Not found.'){
            gigs= []
        }
        unclaimedGigs.value = []
        claimedGigs.value = []
        completeGigs.value = []
        gigs.forEach( gig => {
            if (gig.status == 0){
                unclaimedGigs.value.push(gig)
            } else if (gig.status == 1) {
                claimedGigs.value.push(gig)
            } else if (gig.status == 2) {
                completeGigs.value.push(gig)
            }
        })
    }

    async function cancel(id) {
        await makeRequest('/api/gig/cancel/','post',{
            'gig_id':id
        })
        getData()
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
    <NavSuite title='Feedback' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <main>
        <h1>Claimed</h1>
        <hr/>
        <div class="gig claimed" v-for="(gig, index) in claimedGigs">
            <GigData :gig="gig"/>
            <div class="space-evenly">
                <PinkButton @click-forward="cancel(gig.id)">Cancel</PinkButton>
            </div>
        </div>
        <p v-if="claimedGigs.length == 0">You have no active gigs.</p>
        <h1>Unclaimed</h1>
        <hr/>
        <div class="gig unclaimed" v-for="(gig, index) in unclaimedGigs">
            <GigData :gig="gig"/>
            <div class="space-evenly">
                <PinkButton @click-forward="cancel(gig.id)">Cancel</PinkButton>
            </div>
        </div>
        <p v-if="unclaimedGigs.length == 0">You do not have any pending gigs.</p>
        <h1>Complete</h1>
        <hr/>
        <div class="gig complete" v-for="(gig, index) in completeGigs">
            <GigData :gig="gig"/>
            <div class="space-evenly">
            <PinkButton @click-forward="toggleActiveGig(gig)">Rate Cupid</PinkButton>
            </div>
        </div>
        <p v-if="completeGigs.length == 0">You have no complete gigs.</p>
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
                <PinkButton @click-forward="sendReview">Send</PinkButton>
                <PinkButton @click-forward="toggleActiveGig">Cancel</PinkButton>
            </div>
        </div>
    </main>
</template>

<style scoped>
    .gig {
        border-radius: 12px;
        padding: 12px;
        color: white;
        margin: 6px;
    }
    .gig h1 {
        margin: 0;
    }
    .space-evenly {
        display: flex;
        flex-direction: row;
        align-content: center;
    }
    .claimed {
        background-color: var(--secondary-red);
        border-color: var(--primary-red);
    }
    .unclaimed {
        background-color: var(--secondary-blue);
    }
    .complete {
        background-color: var(--primary-blue);
    }
    .popup {
        position: fixed;
        width: 60%;
        height: 40%;
        max-height: 300px;
        margin: auto;
        left:0;
        right:0;
        top: 30%;

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


