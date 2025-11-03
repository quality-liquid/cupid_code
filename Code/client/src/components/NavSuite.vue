<script setup>
    import router from '../router';
    import { makeRequest, logoutRequest } from '../utils/make_request';
    import { ref, onMounted } from 'vue';

    const props = defineProps(['title', 'profile'])
    const user_id  = parseInt(window.location.hash.split('/')[3])
    const isDarkMode = ref(true);

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
      } else {
        // Set dark mode as default if no preference is saved
        isDarkMode.value = true;
        localStorage.setItem('darkMode', 'true');
      }
      document.documentElement.classList.toggle('dark', isDarkMode.value);
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
                <span class="material-symbols-outlined icon">
                    {{ isDarkMode ? 'light_mode' : 'dark_mode' }}
                </span>
            </button>
            <button id="profile" class="icon-button" @click="naviProf">
                <span class="material-symbols-outlined icon">account_circle</span>
            </button>
        </div>
        <div id="navbar" class="navbar">
            <div class="nav-links">
                <slot />
            </div>
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
  transition: all 0.2s ease;
  color: var(--primary-foreground);
}

.dark-mode-toggle:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: scale(1.05);
}

.dark-mode-toggle:active {
  transform: scale(0.95);
}

.nav-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.nav-links .link {
  display: block;
  padding: 10px 12px;
  background-color: var(--primary);
  color: var(--primary-foreground);
  text-decoration: none;
  border-radius: 6px;
  border: 2px solid transparent;
  transition: all 0.2s ease;
  font-weight: 500;
  margin: 0 8px;
}

.nav-links .link:hover {
  background-color: var(--accent);
  color: var(--accent-foreground);
  transform: translateX(4px);
  border-color: var(--accent-foreground);
}

.nav-links .link:active {
  transform: translateX(2px) scale(0.98);
  background-color: var(--secondary);
}

.logout {
  display: flex;
  align-self: center;
  color: var(--accent-foreground);
  background-color: var(--accent);
  border: 2px solid var(--accent-foreground);
  padding: 10px 12px;
  border-radius: 6px;
  margin: 8px;
  font-weight: 500;
  transition: all 0.2s ease;
  cursor: pointer;
}

.logout:hover {
  background-color: var(--destructive);
  color: var(--destructive-foreground);
  border-color: var(--destructive-foreground);
  transform: translateY(-2px);
}

.logout:active {
  transform: translateY(0) scale(0.98);
}
</style>
