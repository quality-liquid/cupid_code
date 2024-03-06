<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'


</script>

<template>
<div class="container">
  <div class="widget blue">
    <img :src="'/get_chat/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" to="/dater/chat">AI Chat</router-link>
  </div>
  <div class="widget red">
    <img :src="'/get_mic/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" to="/dater/listen">AI Listen</router-link>
  </div>
  <div class="widget blue">
    <img :src="'/get_money/'" alt="Menu Open icon" class="wid_icon">
    <router-link class="header" to="/dater/balance">Add Cash</router-link>
  </div>
  <div class="widget red"> <!-- This will become Calendar when it's made -->
    <router-link class="header" to="/dater/profile">Edit Profile</router-link>
  </div>
</div>
</template>

<style scoped>
  .container {
    margin: 10px;
    margin-top: 50px;
    display: flex;
    flex-flow: row wrap;
    gap: 10px;
  }

  .widget {
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: center;
    padding: 50px;
    border: none;
    border-radius: 16px;
  }

  .header {
    color: white;
  }

  .blue {
    background-color: var(--secondary-blue);
  }

  .red {
    background-color: var(--secondary-red);
  }
</style>