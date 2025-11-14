<script setup>
import { makeRequest } from '../utils/make_request.js';
import { ref } from 'vue';
import router from '../router/index.js';

import PinkButton from '../components/PinkButton.vue'

const email = ref('')
const password = ref('')


async function login() {
    const results = await makeRequest('/api/user/sign_in/', 'post', {
        email: email.value,
        password: password.value,
    })
    if (results.is_suspended) {
        router.push('/suspended')
    }
    else {
        if (results.user['role'].toLowerCase() === 'dater') {
            router.push({name: 'DaterHome', params: {id: results.user['id']}})
        } else if (results.user['role'].toLowerCase() === 'cupid') {
            console.log(results.user['id'])
            router.push({name: 'CupidHome', params: {id: results.user['id']}})
        } else if (results.user['role'].toLowerCase() === 'manager') {
            router.push({name: 'ManagerHome', params: {id: results.user['id']}})
        }
        else {
            router.push('/login')
        }
    }
}

</script>

<template>
    <div class="mobile-container">
        <div class="image">
            <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
        </div>
        <form class="form" @submit.prevent="login">
            <span id="error" class="error">Email or Password is wrong!</span>
            <label class="form_input" for="email">
                Email
                <input type="email" placeholder="example@email.com" id="email" name="email" v-model="email">
            </label>
            <label class="form_input" for="password">
                Password
                <input type="password" placeholder="Password" id="password" name="password" v-model="password">
            </label>
            <PinkButton id="sign_in" type="submit">Sign In</PinkButton>
        </form>
    </div>
    <div class="atag">
        <router-link to="#/register">Get Started Now!</router-link>
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
        background-color: var(--card);
        color: var(--card-foreground);
        border-radius: var(--radius);
        padding: 16px;
        border: 1px solid var(--border);
    }

    .form_input {
        display: flex;
        flex-direction: column;
        padding: 8px;
    }
    input {
        border: 2px solid var(--border);
        border-radius: var(--radius);
        width: auto;
        padding: 8px;
        margin: 10px;
        background-color: var(--input-background);
        color: var(--foreground);
    }

    input:focus {
        outline: none;
        border-color: var(--ring);
        box-shadow: 0 0 0 2px var(--ring);
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
        color: var(--foreground);
        text-decoration: none;
        transition: color 0.2s;
    }

    a:hover {
        color: var(--primary);
    }

    a:visited {
        color: var(--primary);
    }

    .error {
        position: relative;
        left: -300px;
        overflow: hidden;
        color: var(--destructive);
    }

    .shown {
        left: 0px;
        display: flex;
        justify-content: center;
        overflow: visible;
        padding: 10px;
    }
</style>
