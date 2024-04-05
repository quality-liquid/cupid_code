<script setup>
import { makeRequest } from '../utils/make_request';
import {onMounted, ref, watch} from 'vue';

import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

async function getCalendar() {
  const results = await makeRequest(`/api/dater/calendar/${user_id}`);
  // put calendar to screen
}

async function saveDate() {
  // code to save specified date into database
  const results = await makeRequest('/api/dater/', 'post', {
    user: user_id,
    savedDate: date,
  }) 
}



onMounted(() => getCalendar())
</script>

<template>  
    <NavSuite title='Calendar' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <div class="container">
      <h1>Schedule your next date!</h1>
      <p>Only one date can be scheduled at a time. New dates scheduled will overwrite previously scheduled date.</p>
      <!-- This was intended to make it look prettier, but the css doesn't quite work how I inteded it to
        <span class="datepicker-toggle">
        <span class="datepicker-toggle-button"></span>
        <input type="date" class="datepicker-input">
      </span> -->
      <input type="date" name="calendar" class="calendar">
      <button>Submit</button>
    </div>
</template>

<style scoped>
.container {
    margin: 40px;
}
.container h1 {
    margin-top: 50px;
}
.message {
    text-align: center;
    color: white;
    display: flex;
    flex-direction: column;
}
.message h4 {
    margin: 4px;
    margin-top: 0px;
}

/* date input css */
/* .datepicker-toggle {
  display: inline-block;
  position: relative;
  width: 18px;
  height: 19px;
}
.datepicker-toggle-button {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-image: url('data:image/svg+xml;base64,...');
} */



/* supposedly makes it pretty in chrome */
/* .input-container input {
    border: none;
    box-sizing: border-box;
    outline: 0;
    padding: .75rem;
    position: relative;
    width: 100%;
}
input[type="date"]::-webkit-calendar-picker-indicator {
    background: transparent;
    bottom: 0;
    color: transparent;
    cursor: pointer;
    height: auto;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    width: auto;
} */
</style>
