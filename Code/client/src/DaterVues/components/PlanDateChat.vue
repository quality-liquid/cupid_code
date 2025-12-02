<script setup>
import { ref } from 'vue';
import { makeRequest } from '../../utils/make_request';
import PinkButton from '../../components/PinkButton.vue';
import DateForm from './DateForm.vue';

const props = defineProps({
  user_id: {
    type: Number,
    required: true
  }
});

const emit = defineEmits(['close', 'selectDate']);

const message = ref('');
const isLoading = ref(false);
const dateIdeas = ref([]);
const chatMessages = ref([]);
const initialMsg = ref('');
const history = [];

async function initialMessage() {
  const response = await makeRequest(`/api/dateAI/initial_msg`, 'get');
  return response.message[0][1];
}

async function sendMessage() {
  if (chatMessages.value.length === 0 && initialMsg.value) {
    chatMessages.value.push({
      text: initialMsg.value,
      from_ai: true
    });
  }
    
  if (!message.value.trim()) return;

  chatMessages.value.push({
    text: message.value,
    from_ai: false
  });

  const userMessage = message.value;
  message.value = '';
  isLoading.value = true;

  try {
    // TODO: Replace with actual plan-a-date endpoint once backend is ready
    const response = await makeRequest(`/api/dater/plan-date/${props.user_id}/`, 'post', {
      message: userMessage
    });

    if(chatMessages.value.length === 2){
      history.push("role: assistant, content: " + initialMsg.value);
      history.push("role: user, content: " + userMessage);

      //date ideas takes arguments (repsonse, history)
      const aiDateIdeas = await makeRequest(
        `/api/dateAI/date_ideas/?history=${encodeURIComponent(JSON.stringify(history))}`, 'get'
      );
      chatMessages.value.push({
        text: aiDateIdeas.message[0][1],
        from_ai: true
      });

      history.push("role: assistant, content: " + aiDateIdeas.message[0][1]);
    }
    if (chatMessages.value.length > 3){
      history.push("role: user, content: " + userMessage);

      const date = await makeRequest(
        `/api/dateAI/date_plan/?history=${encodeURIComponent(JSON.stringify(history))}`, 'get'
      );

      const dateData = JSON.parse(date.message[0][1]);
      openDateForm(dateData);
    }
  } catch (error) {
    console.error('Error getting date ideas:', error);
    chatMessages.value.push({
      text: 'Sorry, I encountered an error. Please try again later.',
      from_ai: true
    });
  } finally {
    isLoading.value = false;
  }
}

function selectDateIdea(dateIdea) {
  emit('selectDate', dateIdea);
  emit('close');
}

function cancel() {
  chatMessages.value = [];
  emit('close');
}

function openDateForm(dateData) {
  chatMessages.value = [];
  emit('selectDate', dateData);
  emit('close');
}

(async () => {
  initialMsg.value = await initialMessage();
})();

</script>

<template>
  <div class="plan-date-chat">
    <h2>Plan a Date with AI</h2>
    
    <div class="chat-container" id="chat-container">
      <div v-if="chatMessages.length === 0" class="welcome-message">
        <p>{{ initialMsg }}</p>
      </div>
      
      <div 
        v-for="(msg, index) in chatMessages" 
        :key="index" 
        :class="msg.from_ai ? 'chat response' : 'chat sent'"
      >
        <span v-html="msg.text"></span>
      </div>
      
      <div v-if="isLoading" class="chat response">
        Thinking...
      </div>
    </div>

    <div v-if="dateIdeas.length > 0" class="date-ideas">
      <h3>Date Ideas:</h3>
      <div 
        v-for="(idea, index) in dateIdeas" 
        :key="index" 
        class="date-idea-card" 
        @click="selectDateIdea(idea)"
      >
        <div class="idea-header">Option {{ index + 1 }}</div>
        <div class="idea-details">
          <p>
            <strong>When:</strong> 
            {{ idea.date_time ? new Date(idea.date_time).toLocaleString() : 'TBD' }}
          </p>
          <p><strong>Where:</strong> {{ idea.location || 'Location TBD' }}</p>
          <p><strong>What:</strong> {{ idea.description || 'Activity TBD' }}</p>
          <p v-if="idea.budget"><strong>Budget:</strong> ${{ idea.budget.toFixed(2) }}</p>
        </div>
        <div class="idea-action">Click to use this idea</div>
      </div>
    </div>

    <div class="input-section">
      <input 
        type="text" 
        class="message-input" 
        v-model="message" 
        placeholder="Describe your ideal date..."
        @keyup.enter="sendMessage"
        :disabled="isLoading"
      />
      <div class="button-group">
        <PinkButton @click-forward="sendMessage" :disabled="isLoading">Send</PinkButton>
        <PinkButton @click-forward="cancel">Close</PinkButton>
      </div>
    </div>
  </div>
</template>

<style scoped>
.plan-date-chat {
  padding: 16px;
  color: white;
  display: flex;
  flex-direction: column;
  max-height: 80vh;
}

.plan-date-chat h2 {
  margin: 0 0 16px 0;
  text-align: center;
}

.chat-container {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 16px;
  min-height: 200px;
  max-height: 300px;
  padding: 8px;
}

.welcome-message {
  text-align: center;
  padding: 16px;
  color: rgba(255, 255, 255, 0.8);
}

.chat {
  padding: 8px;
  margin: 8px 0;
  border-radius: 4px;
  max-width: 80%;
  word-wrap: break-word;
}

.sent {
  background-color: var(--primary-red);
  color: white;
  margin-left: auto;
  text-align: right;
}

.response {
  background-color: var(--secondary-blue);
  color: white;
  margin-right: auto;
}

.date-ideas {
  margin: 16px 0;
  max-height: 300px;
  overflow-y: auto;
}

.date-ideas h3 {
  margin: 0 0 12px 0;
  text-align: center;
}

.date-idea-card {
  background-color: rgba(255, 255, 255, 0.1);
  border: 2px solid var(--primary-red);
  border-radius: 8px;
  padding: 12px;
  margin: 8px 0;
  cursor: pointer;
  transition: all 0.2s;
}

.date-idea-card:hover {
  background-color: rgba(255, 255, 255, 0.2);
  transform: scale(1.02);
}

.idea-header {
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 8px;
  color: var(--primary-red);
}

.idea-details {
  margin: 8px 0;
}

.idea-details p {
  margin: 4px 0;
  font-size: 0.9em;
}

.idea-action {
  text-align: center;
  margin-top: 8px;
  font-style: italic;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.85em;
}

.input-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: auto;
}

.message-input {
  border: 2px solid rgba(128, 128, 128, 0.5);
  border-radius: 4px;
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

.button-group {
  display: flex;
  justify-content: space-around;
}
</style>
