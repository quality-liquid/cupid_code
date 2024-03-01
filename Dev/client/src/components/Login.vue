<script setup>
import { makeRequest } from '../utils/make_request.js';
import { ref } from 'vue';


const props = defineProps({
  routes: Object,
  currPath: String
})

const email = ref('')
const password = ref('')

async function login() {
    const results = await makeRequest('/sign_in/', 'post', {
        email,
        password
    })
    // Validate response
    
    // Add error class to which one is invalid
    
    // Redirect to dashboard if good
    window.addEventListener('hashchange', () => {
        props.currPath.value = '/#/home';
    })
}

</script>

<template>
        <div class="login_paper">
            <div class="image">
                <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
            </div>
            <form class="form">
                <label class="form_input" for="email">
                    Email
                    <input type="email" placeholder="example@email.com" id="email" name="email" :value="email" @change="(e) => email = e.target.value">
                </label>
                <label class="form_input" for="password">
                    Password
                    <input type="password" placeholder="Password" id="password" name="password" :value="password" @change="(e) => password = e.target.value">
                </label>
                <button class="button" @click="login" type="button">Sign In</button>
            </form>
        </div>
        <div class="atag">
            <a href="#/register">Don't have an Account? Create One!</a>
        </div>
</template>

<style scoped>
    .image {
        display: flex;
        justify-content: center;
        margin-top: 50px;
        border-radius: 16px;
    }
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
        border: 4px var(--secondary-red) solid;
    }

</style>
