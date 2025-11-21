<script setup>
import {ref, computed} from 'vue';
import router from '../router/index.js'
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

</script>

<template>
    <NavSuite title='Home' profile='CupidDetails'>
        <router-link class="link" :to="{name: 'CupidDetails', params: {id: user_id}}">
          Profile 
        </router-link>
        <router-link class="link" :to="{name: 'GigDetails', params: {id: user_id}}">
          Gigs Available 
        </router-link>
        <router-link class="link" :to="{name: 'GigComplete', params: {id: user_id}}">
          Gigs Completed 
        </router-link>
        <router-link class="link" :to="{name: 'CupidFeedback', params: {id: user_id}}">
          Feedback 
        </router-link>
    </NavSuite>


    <div class="mobile-container">
      <router-link class="mobile-button red" :to="{name: 'CupidDetails', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">person</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Profile</div>
          <div class="mobile-button-description">View and edit your profile</div>
        </div>
      </router-link>
      
      <router-link class="mobile-button blue" :to="{name: 'GigDetails', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">explore</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Find Gigs</div>
          <div class="mobile-button-description">Browse available dating assistance gigs</div>
        </div>
      </router-link>
      
      <router-link class="mobile-button red" :to="{name: 'GigComplete', params: {id: user_id}}">
        <span class="material-symbols-outlined mobile-button-icon">playlist_add_check</span>
        <div class="mobile-button-content">
          <div class="mobile-button-title">Past Gigs</div>
          <div class="mobile-button-description">Review your completed gigs</div>
        </div>
      </router-link>
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
