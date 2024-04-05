<script setup>
    import router from '../router';

    const props = defineProps(['title', 'profile'])
    const user_id  = parseInt(window.location.hash.split('/')[3])

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
      const result = await makeRequest(`/logout/`)
      router.push('/')
    }

    function naviProf() {
        router.push({ name: props.profile, params: {id: user_id} })
    }
</script>
<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <span class="material-symbols-outlined icon">menu</span>   
        </button>
        <span>{{ props.title }}</span>
        <button class="icon-button" @click="naviProf">
            <span class="material-symbols-outlined icon">account_circle</span>
        </button>
        <div id="navbar" class="navbar">
            <slot />
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>  
</template>
<style>
</style>
