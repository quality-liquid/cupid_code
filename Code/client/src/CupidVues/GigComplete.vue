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
            <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}"> Profile </router-link>
            <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}"> Gig Details </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>

    <h1>Gig Complete! </h1>
    <form action="">
        <h3>Would you like to rate your dater? </h3>
        <div class="radios">
            <input type="radio">
            <label for="yes">Yes</label>

            <input type="radio">
            <label for="no">No</label>
        </div>        

        <div>
            <label for="daterRating"> How would you rate the dater you serviced? (between 0 and 5):</label>
            <input type="range" id="daterRating" name="daterRating" min="0" max="5">
        </div>

        <div>
            <label for="comments">Any issues or complements you would like to include? </label>
            <input type="text">
        </div>

        <button>Submit</button>
    </form>
</template>

<style scoped>
</style>
