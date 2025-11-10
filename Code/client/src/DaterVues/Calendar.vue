<script setup>
import { ref, computed, onMounted } from 'vue'
import { Calendar } from 'v-calendar'
import 'v-calendar/style.css'

import { makeRequest } from '../utils/make_request'
import NavSuite from '../components/NavSuite.vue'
import Popup from '../components/Popup.vue'
import DateForm from './components/DateForm.vue'
import PlanDateChat from './components/PlanDateChat.vue'
import PinkButton from '../components/PinkButton.vue'

const user_id = parseInt(window.location.hash.split('/')[3])

const dates = ref([])
const showDateForm = ref(false)
const showPlanChat = ref(false)
const dateFormData = ref(null)

const attributes = computed(() =>
  dates.value.map((date) => ({
    key: date.id,
    dates: [new Date(date.date_time)],
    dot: {
      color:
        date.status === 'planned'
          ? 'var(--secondary-red)'
          : date.status === 'occurring'
          ? 'var(--primary-red)'
          : date.status === 'completed'
          ? 'var(--secondary-blue)'
          : 'gray',
    },
    popover: {
      visibility: 'hover',
    },
    popoverLabel: `${date.location} - ${date.description}`,
  }))
)

async function getCalendar() {
  try {
    const results = await makeRequest(`/api/dater/calendar/${user_id}/`)
    dates.value = results || []
  } catch (error) {
    console.error('Error fetching calendar:', error)
    dates.value = []
  }
}

function openAddDateForm() {
  dateFormData.value = null
  showDateForm.value = true
}

function openPlanChat() {
  showPlanChat.value = true
}

function closeDateForm() {
  showDateForm.value = false
  dateFormData.value = null
}

function closePlanChat() {
  showPlanChat.value = false
}

function handleDateSelected(dateIdea) {
  dateFormData.value = {
    date_time: dateIdea.date_time || '',
    location: dateIdea.location || '',
    description: dateIdea.description || '',
    budget: dateIdea.budget || 0.0,
  }
  showPlanChat.value = false
  showDateForm.value = true
}

function handleDateSuccess() {
  getCalendar()
}

onMounted(() => getCalendar())
</script>

<template>
  <NavSuite title="Calendar" profile="DaterProfile">
    <router-link class="link" :to="{ name: 'DaterHome', params: { id: user_id } }">Home</router-link>
    <router-link class="link" :to="{ name: 'DaterProfile', params: { id: user_id } }">Profile</router-link>
    <router-link class="link" :to="{ name: 'AiChat', params: { id: user_id } }">AI Chat</router-link>
    <router-link class="link" :to="{ name: 'AiListen', params: { id: user_id } }">AI Listen</router-link>
    <router-link class="link" :to="{ name: 'DaterGigs', params: { id: user_id } }">Gigs</router-link>
    <router-link class="link" :to="{ name: 'CupidCash', params: { id: user_id } }">Balance</router-link>
    <router-link class="link" :to="{ name: 'DaterFeedback', params: { id: user_id } }">Feedback</router-link>
  </NavSuite>

  <div class="mobile-container">
    <div class="header">
      <h2>View Upcoming Dates and Add New Dates!</h2>
      <div class="button-group">
        <PinkButton @click-forward="openAddDateForm">Add Date</PinkButton>
        <PinkButton @click-forward="openPlanChat">Plan a date w/ AI</PinkButton>
      </div>
    </div>

    <div class="calendar-container">
      <Calendar
        :attributes="attributes"
        :columns="2"
        :rows="1"
        expanded
        class="calendar"
      />
    </div>

    <div class="dates-list" v-if="dates.length > 0">
      <h3>Upcoming Dates</h3>
      <div v-for="date in dates" :key="date.id" class="date-item">
        <div class="date-info">
          <h4>
            {{ new Date(date.date_time).toLocaleDateString() }}
            at
            {{
              new Date(date.date_time).toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit',
              })
            }}
          </h4>
          <p><strong>Location:</strong> {{ date.location }}</p>
          <p><strong>Description:</strong> {{ date.description }}</p>
          <p v-if="date.budget"><strong>Budget:</strong> ${{ parseFloat(date.budget).toFixed(2) }}</p>
          <p><strong>Status:</strong> {{ date.status }}</p>
        </div>
      </div>
    </div>

    <p v-else class="no-dates">No dates scheduled yet. Add one to get started!</p>
  </div>

  <Popup :data-active="showDateForm">
    <DateForm
      :user_id="user_id"
      :initialData="dateFormData"
      @close="closeDateForm"
      @success="handleDateSuccess"
    />
  </Popup>

  <Popup :data-active="showPlanChat">
    <PlanDateChat
      :user_id="user_id"
      @close="closePlanChat"
      @selectDate="handleDateSelected"
    />
  </Popup>
</template>

<style scoped>
.mobile-container {
  padding: 20px;
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-bottom: 4px solid var(--primary-red);
  color: var(--secondary-blue);
  padding-bottom: 20px;
  margin-bottom: 20px;
}

.header h2 {
  margin: 8px;
  margin-bottom: 16px;
  color: var(--secondary-blue);
}

.button-group {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.calendar-container {
  margin: 20px 0;
  display: flex;
  justify-content: center;
}

.calendar {
  width: 100%;
  max-width: 800px;
}

.dates-list {
  margin-top: 30px;
}

.dates-list h3 {
  color: var(--secondary-blue);
  margin-bottom: 16px;
}

.date-item {
  background-color: var(--secondary-blue);
  color: white;
  border-radius: 8px;
  padding: 16px;
  margin: 12px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.date-info h4 {
  margin: 0 0 8px 0;
  color: var(--primary-red);
}

.date-info p {
  margin: 4px 0;
}

.no-dates {
  text-align: center;
  color: var(--secondary-blue);
  margin-top: 20px;
  font-style: italic;
}

:deep(.vc-container) {
  border: 2px solid var(--primary-red);
  border-radius: 8px;
}

:deep(.vc-weeks) {
  padding: 8px;
}

:deep(.vc-weekday) {
  color: var(--secondary-blue);
  font-weight: bold;
}

:deep(.vc-day-content:hover) {
  background-color: var(--secondary-red);
  color: white;
}

:deep(.date-dot) {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
</style>
