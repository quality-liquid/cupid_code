<script setup>
import { ref, onMounted } from 'vue';
function naviProf() {
    router.push({ name: 'DaterProfile', params: {id: user_id} })
}
</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
        </button>
        <!-- This will be the profile picture when setup -->
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
            <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
            <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
            <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
            <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance </router-link>
            <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>
    <div>Under construction</div>
</template>

<style scoped>

</style>
