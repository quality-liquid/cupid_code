<script>
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
}


export default {
  name: 'Login'
};

</script>

<template>
    <div class="login_paper">
        <img :src="'/get_img/'" alt="Cupid Code Logo">
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
    .login_paper {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: var(--primary-blue);
    }

    .button {
        background-color: var(--secondary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
    }

    .form {
        display: flex;
        flex-flow: column wrap;
    }
    .form_input {
        display: flex;
        flex-direction: column;
    }

</style>
