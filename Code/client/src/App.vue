<script setup>
import router from './router/index.js';
import { makeRequest } from './utils/make_request.js';
import { ref, onMounted } from 'vue';

const user_id = parseInt(window.location.hash.split('/')[3])
const isDarkMode = ref(true);

async function getUser() {
  const results = await makeRequest('api/user/', 'get', {
    user_id: user_id
  })
}

function toggleDarkMode() {
  isDarkMode.value = !isDarkMode.value;
  document.documentElement.classList.toggle('dark', isDarkMode.value);
  localStorage.setItem('darkMode', isDarkMode.value);
}

onMounted(() => {
  const savedDarkMode = localStorage.getItem('darkMode');
  if (savedDarkMode !== null) {
    isDarkMode.value = savedDarkMode === 'true';
  } else {
    // Set dark mode as default if no preference is saved
    isDarkMode.value = true;
    localStorage.setItem('darkMode', 'true');
  }
  document.documentElement.classList.toggle('dark', isDarkMode.value);
});
</script>

<template>
    <div id="app">
      <nav class="nav">
          <router-link id="login" class="link" to="/login"> Login </router-link>
          <router-link id="sign up" class="link" to="/register"> Sign Up </router-link>
          <router-link id="welcome" class="link" to="/"> Welcome </router-link>
          <button @click="toggleDarkMode" class="dark-mode-toggle">
            {{ isDarkMode ? '☀️' : '🌙' }}
          </button>
      </nav>
    </div>
    <router-view />
</template>

<style scoped>
.dark-mode-toggle {
  background: none;
  border: none;
  font-size: 1.2em;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.2s;
  color: var(--primary-foreground);
}

.dark-mode-toggle:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
