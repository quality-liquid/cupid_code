<template>
  <div id="app">
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Sign Up</router-link>
  
    <router-view></router-view>
  </div>
</template>
  

<script>
export default {
  name: 'App'
};
</script>