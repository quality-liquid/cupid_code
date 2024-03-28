<script setup>
    import router from '../router/index'
    import { makeRequest } from '../utils/make_request'
    import {ref, onMounted} from 'vue'

    import CupidCoin from './CupidCoin.vue'

    //User info
    const user_id  = parseInt(window.location.hash.split('/')[3]) //Gets the id from the router
    const email = ref('')
    const phone = ref('')
    const fname = ref('')
    const lname = ref('')
    const username = ref('')

    //Cupid info
    const accepting_gigs = ref(false)
    const balance = ref(0)
    const range = ref(20)
    const gigs_completed = ref(0)
    const gigs_failed = ref(0)

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

    async function update() {
        // Validate data
        const checkData = [email, phone]

        let check = 0;
        for (let i = 0; i < checkData.length; i++) {
            if (checkData[i] !== '') check++;
            else {
                const error = document.querySelector(`input[name=${checkData[i]}]`);
                error.class = error.class + 'error';
            }
        }
        const results = await makeRequest(`/api/cupid/profile/`, 'post', {
            first_name: fname.value,
            last_name: lname.value,
            phone_number: phone.value,
            gig_range: range.value
        })
        router.push({name: 'CupidDetails', params: {id: user_id}});
    }

    async function getData() {
        const cupid = await makeRequest(`api/user/${user_id}`)
        email.value = cupid.user.email
        phone.value = cupid.user.phone_number
        fname.value = cupid.user.first_name
        lname.value = cupid.user.last_name
        username.value = cupid.user.username

        accepting_gigs.value = cupid.accepting_gigs
        balance.value = cupid.cupid_cash_balance
        range.value = cupid.gig_range
        gigs_completed.value = cupid.gigs_completed
        gigs_failed.value = cupid.gigs_failed
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
            <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gig Details </router-link>
            <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}"> Check Completed </router-link>
 11           <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>
    <main> 
        <label for="accepting_gigs">
            Accepting Gigs
            <input type="checkbox" v-model="accepting_gigs"/>
        </label>
        <CupidCoin :active="accepting_gigs"/>
        <div class="card">
            <p>${{ balance }}</p>
            <hr></hr>
            <p>{{ gigs_completed }} / {{ gigs_failed + gigs_completed}} succesful gigs</p>
        </div>
        <h1>Update Details</h1>
        <hr>
        <form class="container" @submit.prevent="update">
            <label class="update-content" for="fname">
                First Name
                <input type="text" id="fname" v-model="fname"/>
            </label>
            <label class="update-content" for="lname">
                Last Name
                <input type="text" id="lname" v-model="lname"/>
            </label>
            <label class="update-content" for="phone">
                Phone Number
                <input type="number" id="phone" :placeholder="phone" v-model="phone"/>
            </label>
            <label class="update-content" for="range">
                Range
                <input type="text" id="range" v-model="range"/>
            </label>
            <button class="button">Save</button>
        </form>
    </main>
</template>

<style scoped>

main {
    position: absolute;
    top: 42px;
    left: 0px;
    right: 0px;
}

hr {
    border: 1px solid #F0F0F0;
    border-radius: 30%;
    margin: 6px;
}

.update-content {
    display: flex;
    flex-direction: column;
    padding: 8px;
    margin: 10px;
    font-weight: bold;
}

input {
    border: 3px rgba(128, 128, 128, 0.5) solid;
    border-radius: 4px;
    width: auto;
    padding: 8px;
    margin: 10px;
}

.button {
    width: auto;
    background-color: var(--primary-red);
    border-radius: 10px;
    color: white;
    border: none;
    border-radius: 4px;
    box-shadow: 5px 5px 2px rgba(128, 128, 128, 0.5);
    text-decoration: solid;
    padding: 16px;
    margin: auto;
    display: flex;
    justify-self: center;
    align-self: center;
}

.card {
    border: 4px solid var(--secondary-blue);
    border-radius: 16px;
    margin: 16px;
    padding: 8px;
    background-color: var(--primary-blue);
    color: white;
    font-size: 1.3em;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.card > hr {
    border-color: var(--secondary-red);
}
.card > p {
    margin-top: 2px;
    margin-bottom: 2px;
    margin-left: auto;
    margin-right: auto;
}
</style>
