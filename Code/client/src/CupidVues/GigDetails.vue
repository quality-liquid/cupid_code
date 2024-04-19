<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    import NavSuite from '../components/NavSuite.vue';
    import GigData from './components/GigData.vue'
    import PinkButton from '../components/PinkButton.vue'

    const gigCount = 0
    const gigs = ref([])
    const activeGigs = ref([])
    const reward = ref(0)
    const rewardShow = ref(false)

    const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router

    async function getData() {
        gigs.value = await makeRequest(`api/gig/${user_id}/${gigCount}`)
        activeGigs.value = await makeRequest(`api/cupid/gigs/${user_id}?complete=false`)
        //Django returns a 404 if there none of either of these. We have to tell Vue it is ok.
        if (gigs.value.detail === 'Not found.'){
            gigs.value = []
        }
        if (activeGigs.value.detail === 'Not found.'){
            activeGigs.value = []
        }
    }

    function displayReward(amount) {
        reward.value = amount
        rewardShow.value = true
        setTimeout(() => {rewardShow.value = false},1500)
    }

    async function claim(id) {
        await makeRequest('/api/gig/accept/','post',{
            'gig_id':id
        })
        getData()
    }

    async function complete(id) {
        const response = await makeRequest('/api/gig/complete/','post',{
            'gig_id':id
        })
        getData()
        displayReward(response.reward)
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
    <NavSuite title='Gigs' profile='CupidDetails'>
        <router-link class="link" :to="{name: 'CupidHome', params: {id: user_id}}"> Home </router-link>
        <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
        <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}"> Gigs Completed </router-link>
        <router-link class="link" :to="{name: 'CupidFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <main>
        <h1>Active</h1>
        <hr/>
        <div class="gig active" v-for="(gig, index) in activeGigs">
            <GigData :gig="gig"/>
            <div class="space-evenly">
                <PinkButton @click-forward="complete(gig.id)">Complete</PinkButton>
                <PinkButton @click-forward="drop(gig.id)">Drop</PinkButton>
            </div>
        </div>
        <p v-if="activeGigs.length == 0">You are not currently on any gigs.</p>
        <h1>Available</h1>
        <hr/>
        <div class="gig inactive" v-for="(gig, index) in gigs">
            <GigData :gig="gig"/>
            <PinkButton @click-forward="claim(gig.id)">Claim</PinkButton>
        </div>
        <p v-if="gigs.length == 0">There are no gigs available.</p>
        <p class="bottom" :data-active="rewardShow">+ ${{ reward.toFixed(2) }}</p>
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
        align-content: space-evenly;
    }
    .active {
        background-color: var(--secondary-red);
        border-color: var(--primary-red);
    }
    .inactive {
        background-color: var(--secondary-blue);
    }
    @keyframes reward {
        from {
            bottom: 0;
            color: #00FF00FF;
        }
        to {
            bottom: 2em;
            color: #00FF0000;
        }
    }
    .bottom {
        position: fixed;
        height: 2em;
        width: 200px;
        bottom: -2em;
        left: 50%;
        margin-left: -100px;
        color: #00FF00FF;
        font-size: 3em;
        text-align: center;
    }
    .bottom[data-active="true"] {
        bottom: 2em;
        animation-name: reward;
        animation-duration: 1.5s;
        animation-timing-function: linear;
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
