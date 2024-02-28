<template>
  <div id="app">
    <router-link :to="{ name: '', hash: '#login' }">Login</router-link>
    <router-link :to="{name: '', hash: '#register'}">Sign Up</router-link>
    <router-link to="/"> Back </router-link>
    <router-view></router-view>
  </div>
</template>
  

<script>
export default {
  name: 'App'
};
</script>