<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

</script>

<template>
  <div class="dater-home-root">
    <NavSuite title='Home' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    <router-link class="link" :to="{ name: 'NotificationCenter', params: {id: user_id}}"> Notifications </router-link>
        <a to="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Need Help?</a>
    </NavSuite>

    <div class="mobile-container">
      <router-link class="mobile-button blue" :to="{name: 'AiChat', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">forum</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">AI Chat</div>
          <div class="mobile-button-description">Chat with your AI dating assistant</div>
        </div>
      </router-link>
      
      <router-link class="mobile-button red" :to="{name: 'AiListen', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">mic</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">AI Listen</div>
          <div class="mobile-button-description">Get real-time advice during dates</div>
        </div>
      </router-link>
      
      <router-link class="mobile-button blue" :to="{name: 'CupidCash', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">attach_money</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Add Cash</div>
          <div class="mobile-button-description">Manage your Cupid Cash balance</div>
        </div>
      </router-link>
      
      <router-link class="mobile-button red" :to="{name: 'Calendar', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">calendar_month</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Calendar</div>
          <div class="mobile-button-description">Schedule and track your dates</div>
        </div>
      </router-link>
      <router-link class="mobile-button blue" :to="{name: 'NotificationCenter', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">notifications</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Notifications</div>
          <div class="mobile-button-description">Manage push notifications</div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
  .blue {
    background-color: var(--secondary-blue);
  }

  .red {
    background-color: var(--secondary-red);
  }
</style>
