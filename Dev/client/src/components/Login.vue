<script setup>
import { makeRequest } from '../utils/make_request.js';
import { ref } from 'vue';
import router from '../router/index.js';

const email = ref('')
const password = ref('')


async function login() {
    const results = await makeRequest('/api/user/sign_in/', 'post', {
        email: email.value,
        password: password.value,
    })
    // Add error class to which one is invalid
    const doc = document.getElementById('error')
    if (results.method === '400' || results.method === 400) {
        doc.className = 'error shown'
        return;
    }
    else {
        doc.className = 'error'
    }
    
    // Redirect to dashboard if good
    if (results.user['role'].toLowerCase() === 'dater') {
        router.push({name: 'DaterHome', params: {id: results.user['id']}})
    } else if (results.user['role'].toLowerCase() === 'cupid') {
        router.push({name: 'CupidHome', params: {id: results.user['id']}})
    } else if (results.user['role'].toLowerCase() === 'manager') {
        router.push({name: 'ManagerHome', params: {id: results.user['id']}})
    }
    else {
        router.push('/login')
    }
}

</script>

<template>
    <div class="login_paper">
        <div class="image">
            <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
        </div>
        <form class="form" @submit.prevent="login">
            <span id="error" class="error">Email or Password is wrong!</span>
            <label class="form_input" for="email">
                Email
                <input type="email" placeholder="example@email.com" id="email" name="email" :value="email" @change="(e) => email = e.target.value">
            </label>
            <label class="form_input" for="password">
                Password
                <input type="password" placeholder="Password" id="password" name="password" :value="password" @change="(e) => password = e.target.value">
            </label>
            <button class="button">Sign In</button>
        </form>
    </div>
    <div class="atag">
        <a href="#/register">Don't have an Account? Create One!</a>
    </div>
</template>

<style scoped>
    .login_paper {
        display: flex;
        flex-flow: column wrap;
    }
    .button {
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
        box-shadow: 5px 5px 2px rgba(128, 128, 128, 0.5);
    }

    .form {
        display: flex;
        flex-flow: column wrap;
        background-color: white;
    }

    .form_input {
        display: flex;
        flex-direction: column;
        padding: 8px;
    }
    input {
        border: 3px rgba(128, 128, 128, 0.5) solid;
        border-radius: 4px;
        width: auto;
        padding: 8px;
        margin: 10px;
    }

    .button {
        margin: 10px;
        padding: 16px;
        border: none;
        border-radius: 8px;
    }

    .atag {
        display: flex;
        margin: 10px;
        justify-content: center;
    }
    a {
        margin: 10px;
        color: white;
    }

    a:hover {
        color: white;
    }

    a:visited {
        color: var(--primary-red);
    }

    .error {
        position: relative;
        left: -300px;
        overflow: hidden;
        color: var(--secondary-red);
    }

    .shown {
        left: 0px;
        display: flex;
        justify-content: center;
        overflow: visible;
        padding: 10px;
    }
</style>
