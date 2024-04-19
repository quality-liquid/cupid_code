<script setup>
import { makeRequest } from '../utils/make_request';
import {onMounted, ref} from 'vue';
import NavSuite from '../components/NavSuite.vue';

const user_id  = parseInt(window.location.hash.split('/')[3])

const newDate = ref('')
const addr = ref('')
const desc = ref('')
const budget = ref(0.0)

async function getCalendar() {
  const results = await makeRequest(`/api/dater/calendar/${user_id}/`);
  const dates = document.getElementById('dates')
  console.log(results)
  // put calendar to screen
  for (let res of results) {
    const date = document.createElement('div')
    date.setAttribute('class', 'date')
    date.setAttribute('id', res.id)
    date.innerHTML = `
      <h3>${res.date_time.split('T')[0]}</h3>
      <span>${res.location}</span>
      <span>${res.description}</span>
      <span >${res.status}</span>
    `
    const button = document.createElement('button')
    button.setAttribute('class', "button")
    button.setAttribute('onclick', `${() => {
      if (res.status === 'planned') res.status = 'completed'
      else res.status = 'planned'
    } }`)
    button.innerText = 'Change Status'
    date.appendChild(button)
    dates.appendChild(date)
  }
}

async function addDate() {
  console.log(newDate.value)
  // Add to screen
  const dates = document.getElementById('dates')

  const res = await makeRequest(`/api/dater/calendar/${user_id}/`, 'post', {
    date_time: newDate.value,
    location: addr.value,
    description: desc.value,
    status: 'planned',
    budget: budget.value,
  })

  const date = document.createElement('div')
  date.setAttribute('class', 'date')
  date.setAttribute('id', res.id)
  date.innerHTML = `
    <h3>${res.date_time.split('T')[0]}</h3>
    <span>${res.location}</span>
    <span>${res.status}</span>
  `
  const button = document.createElement('button')
  button.setAttribute('class', "button")
  button.setAttribute('onclick', `${() => {
    if (res.status === 'planned') res.status = 'completed'
    else res.status = 'planned'
  } }`)
  button.innerText = 'Change Status'
  date.appendChild(button)
  dates.appendChild(date)
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
      <div class="header">
        <h2>View Upcoming Dates and Add New Dates!</h2>
        <form class="form" @submit.prevent="addDate">
          <label for="date">
            Choose the Day
          </label>
          <input type="date" class="add-date" id="date" v-model="newDate">
          <label for="addr">
            Where are you Going?
          </label>
          <input type="text" class="add-date" id="addr" v-model="addr">
          <label for="desc">
            What will you be doing?
          </label>
          <input type="desc" class="add-date" id="desc" v-model="desc">
          <label for="budget">
            Max budget for Gigs ($XX.XX)
          </label>
          <input type="number" class="add-date" id="budget" v-model="budget">
          <button class="button">Add!</button>
        </form class="form">
      </div>

      <div class="dates" id="dates">

      </div>
    </div>
</template>

<style scoped>
.container {
  margin: 40px;
  margin-top: 50px;
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-bottom: 4px solid var(--primary-red);
  color: var(--secondary-blue);
}

.header h2 {
  margin: 8px;
  margin-bottom: 0px;
  color: var(--secondary-blue);
}

.form {
  display: flex;
  flex-flow: column wrap;
  margin: 20px;
  margin-top: 5px;
  gap: 8px;
}

.form label {
  text-align: center;
  font-weight: bold;
}

.add-date {
  border: 2px solid rgba(128, 128, 128, 0.5);
  border-radius: 4px;
  padding: 8px;
}

.button {
    display: flex;
    justify-content: center;
    background-color: var(--secondary-red);
    border: none;
    border-radius: 4px;
    padding: 8px;
    margin: 2px 4px;
    color: white;
    box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
}

.button:hover {
    filter: brightness(.7);
}
</style>
