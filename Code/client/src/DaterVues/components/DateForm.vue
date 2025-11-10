<script setup>
import { ref, watch } from 'vue';
import { makeRequest } from '../../utils/make_request';
import PinkButton from '../../components/PinkButton.vue';

const props = defineProps({
  user_id: {
    type: Number,
    required: true
  },
  initialData: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['close', 'success']);

const dateTime = ref('');
const location = ref('');
const description = ref('');
const budget = ref(0.0);

watch(() => props.initialData, (newData) => {
  if (newData) {
    dateTime.value = newData.date_time || '';
    location.value = newData.location || '';
    description.value = newData.description || '';
    budget.value = newData.budget || 0.0;
  }
}, { immediate: true });

async function submitDate() {
  if (!dateTime.value || !location.value || !description.value) {
    alert('Please fill in all required fields');
    return;
  }

  try {
    const res = await makeRequest(`/api/dater/calendar/${props.user_id}/`, 'post', {
      date_time: dateTime.value,
      location: location.value,
      description: description.value,
      status: 'planned',
      budget: budget.value,
    });
    
    emit('success', res);
    emit('close');
    
    dateTime.value = '';
    location.value = '';
    description.value = '';
    budget.value = 0.0;
  } catch (error) {
    console.error('Error creating date:', error);
    alert('Failed to create date. Please try again.');
  }
}

function cancel() {
  emit('close');
  dateTime.value = '';
  location.value = '';
  description.value = '';
  budget.value = 0.0;
}
</script>

<template>
  <div class="date-form">
    <h2>Add Date</h2>
    <form @submit.prevent="submitDate">
      <label class="form-label" for="date">
        Choose the Day
      </label>
      <input type="date" class="form-input" id="date" v-model="dateTime" required>
      
      <label class="form-label" for="location">
        Where are you Going?
      </label>
      <input type="text" class="form-input" id="location" v-model="location" required>
      
      <label class="form-label" for="description">
        What will you be doing?
      </label>
      <textarea class="form-input" id="description" v-model="description" required></textarea>
      
      <label class="form-label" for="budget">
        Max budget for Gigs ($XX.XX)
      </label>
      <input type="number" step="0.01" class="form-input" id="budget" v-model="budget" min="0">
      
      <div class="button-group">
        <PinkButton @click-forward="submitDate">Submit</PinkButton>
        <PinkButton @click-forward="cancel">Cancel</PinkButton>
      </div>
    </form>
  </div>
</template>

<style scoped>
.date-form {
  padding: 16px;
  color: white;
}

.date-form h2 {
  margin: 0 0 16px 0;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.form-label {
  text-align: center;
  font-weight: bold;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-input {
  border: 2px solid rgba(128, 128, 128, 0.5);
  border-radius: 4px;
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

textarea.form-input {
  min-height: 80px;
  resize: vertical;
}

.button-group {
  display: flex;
  justify-content: space-around;
  margin-top: 8px;
}
</style>

