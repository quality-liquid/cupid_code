<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

</script>

<template>
    <NavSuite title='Home' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
        <a to="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Need Help?</a>
    </NavSuite>

    <div class="container">
      <div class="widget blue">
        <span class="material-symbols-outlined icon">forum</span>
        <router-link class="header" :to="{name: 'AiChat', params: {id: user_id}}">AI Chat</router-link>
      </div>
      <div class="widget red">
        <span class="material-symbols-outlined icon">mic</span>
        <router-link class="header" :to="{name: 'AiListen', params: {id: user_id}}">AI Listen</router-link>
      </div>
      <div class="widget blue">
        <span class="material-symbols-outlined icon">attach_money</span>
        <router-link class="header" :to="{name: 'CupidCash', params: {id: user_id}}">Add Cash</router-link>
      </div>
      <div class="widget red"> <!-- This will become Calendar when it's made -->
        <span class="material-symbols-outlined icon">calendar_month</span>
        <router-link class="header" :to="{name: 'Calendar', params: {id: user_id}}">Calendar</router-link>
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
