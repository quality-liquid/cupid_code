<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'


</script>

<template>
<div class="container">
  <div class="widget blue">
    <router-link class="header" to="/dater/chat">AI Chat</router-link>
  </div>
  <div class="widget red">
    <router-link class="header" to="/dater/listen">AI Listen</router-link>
  </div>
  <div class="widget blue">
    <router-link class="header" to="/dater/balance">Add Cash</router-link>
  </div>
  <div class="widget red"> <!-- This will become Calendar when it's made -->
    <router-link class="header" to="/dater/profile">Edit Profile</router-link>
  </div>
</div>
</template>

<style scoped>
  .container {
    display: flex;
    flex-flow: row wrap;
  }

  .widget {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 50px;
    border: none;
    border-radius: 16px;
  }

  .blue {
    background-color: var(--secondary-blue);
  }

  .red {
    background-color: var(--secondary-red);
  }
</style>