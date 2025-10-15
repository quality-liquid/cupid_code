<script setup>
    import router from '../router';
    import { makeRequest, logoutRequest } from '../utils/make_request';
    import { ref, onMounted } from 'vue';

    const props = defineProps(['title', 'profile'])
    const user_id  = parseInt(window.location.hash.split('/')[3])
    const isDarkMode = ref(false);

    function openDrawer() {
      const element = document.getElementById('navbar')
      if (element.className === 'navbar') {
        element.className = 'navbar opened'
      }
      else {
        element.className = 'navbar'
      }
    }

    async function logout() {
      await logoutRequest()
      await router.push('/')
      router.go()
    }

    function naviProf() {
        router.push({ name: props.profile, params: {id: user_id} })
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
        document.documentElement.classList.toggle('dark', isDarkMode.value);
      }
    });
</script>
<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <span id="navMenu" class="material-symbols-outlined icon">menu</span>   
        </button>
        <span id="title">{{ props.title }}</span>
        <div class="nav-controls">
            <button @click="toggleDarkMode" class="dark-mode-toggle">
                {{ isDarkMode ? '☀️' : '🌙' }}
            </button>
            <button id="profile" class="icon-button" @click="naviProf">
                <span class="material-symbols-outlined icon">account_circle</span>
            </button>
        </div>
        <div id="navbar" class="navbar">
            <slot />
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>  
</template>
<style scoped>
.nav-controls {
  display: flex;
  align-items: center;
  gap: 8px;
}

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
