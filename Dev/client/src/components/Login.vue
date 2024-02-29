<script setup>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

const email = ref('')
const password = ref('')

async function login() {
    await makeRequest('/sign_in/', 'post', {
        email,
        password
    })
    // Validate response

    // Redirect to dashboard if good

    // Add error class to which one is invalid
}

</script>

<template>
    <div class="image">
        <img :src="'/get_img/'" alt="Cupid Code Logo" width="200" height="200">
    </div>
    <div class="login_paper">
        <form class="form">
            <label class="form_input" for="email">
                Email
                <input type="email" name="email" :value="email" @change="(e) => email = e.target.value">
            </label>
            <label class="form_input" for="password">
                Password
                <input type="password" name="password" :value="password" @change="(e) => password = e.target.value">
            </label>
            <button class="button" @click="login">Sign In</button>
        </form>
    </div>
</template>

<style scoped>
    .image {
        display: flex;
        margin-top: 50px;
        border-radius: 16px;
    }
    .login_paper {
        display: flex;
        margin-top: 20px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: var(--secondary-blue);
        border-radius: 16px;
        color: white;
    }

    .button {
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
    }

    .form {
        display: flex;
        flex-flow: column wrap;
        justify-content: center;
        align-items: center;
    }

    .form_input {
        margin: 4px;
        text-align: center;
    }

    input {
        display: flex;
        flex-direction: column;
        border: none;
        padding: 16px;
        border-radius: 8px;
        margin: 8px;
    }

    .button {
        margin: 10px;
        padding: 16px;
        border: none;
        border-radius: 8px;
    }

    .error {
        border: 4px var(--secondary-red) solid;
    }

</style>
