<script setup>
import router from './router/index.js';
import { makeRequest } from './utils/make_request.js';

const user_id = parseInt(window.location.hash.split('/')[3])

async function getUser() {
  const results = await makeRequest('api/user/', 'get', {
    user_id: user_id
  })
}
</script>

<template>
    <div id="app">
      <nav class="nav">
          <router-link class="link" to="/login"> Login </router-link>
          <router-link class="link" to="/register"> Sign Up </router-link>
          <router-link class="link" to="/"> Welcome </router-link>
      </nav>
    </div>
    <router-view />
</template>

<style scoped>

</style>
