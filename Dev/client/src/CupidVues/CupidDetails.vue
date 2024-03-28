<script setup>
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
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>
        <h1><br/>You are in CupidDetails.vue</h1>
    
    <div>
        <h2>Total Earned</h2>
        <p>cupid.totalearned</p>
    </div>

    <div>
        <h2>Next Payment</h2>
        <p>nextPayment</p>
    </div>
</template>

<style scoped>
</style>
