<script setup>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

console.log('Routed to Register')

const email = ref('')
const password = ref('')
const accType = ref('')
const fname = ref('')
const lname = ref('')
const addr = ref('')
const image = ref()

async function register() {
    // Validate data 
    await makeRequest('/sign_in/', 'post', {
        email,
        password,
        accType,

    })
    // Redirect to dashboard
}

</script>

<template>
    <div class="image">
        <img :src="'/get_img/'" alt="Cupid Code Logo" width="200" height="200">
    </div>
    <div class="container">
        <h1>Create Your Account!</h1>
        <form class="form">
            <label class="input_detail" for="email">
                Email
                <input type="email" :value="email" @change="(e) => email = e.target.value"/>
            </label>
            <label class="input_detail" for="password">
                Password
                <input type="password" :value="password" @change="(e) => password = e.target.value"/>
            </label>
            <label class="input_detail" for="fname">
                First Name
                <input type="text" :value="fname" @change="(e) => fname = e.target.value"/>
            </label>
            <label class="input_detail" for="lname">
                Last Name
                <input type="text" :value="lname" @change="(e) => lname = e.target.value"/>
            </label>
            <label class="input_detail" for="image">
                Profile Picture
                <input type="image" name="image" :value="image" @change="(e) => image = e.target.value"/>
            </label>
            <label class="input_detail" for="address">
                Address
                <input type="text" :value="addr" @change="(e) => addr = e.target.value"/>
            </label>
            <div class="radios">
                Account Type
                <label class="radio_detail" for="cupid">
                    Cupid
                    <input type="radio" id="cupid" name="accountType" :value="accType" />
                </label>
                <label class="radio_detail" for="dater">
                    Dater
                    <input type="radio" id="dater" name="accountType" :value="accType" />
                </label>
            </div>
            <div v-if="accType.toLowerCase === 'dater'">
                <label>
                    Dating Weaknesses
                    <textarea></textarea>
                </label>
                <label>
                    Dating Strengths
                    <textarea></textarea>
                </label>
            </div>
            <div v-else-if="accType.toLowerCase === 'cupid'">

            </div>

            <button class="button" @click="register">Create Account</button>
        </form>
    </div>
</template>

<style scoped>
    .image {
        display: flex;
        margin-top: 50px;
        border-radius: 16px;
    }
    .container {
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

    .input_detail {
        margin: 4px;
        text-align: center;
    }

    .radios {
        display: flex;
        flex-flow: column wrap;
    }

    input {
        display: flex;
        flex-direction: column;
        border: none;
        padding: 16px;
        border-radius: 8px;
        margin: 8px;
    }

    input[name="accountType"] {
        display: flex;
        border: none;
        color: var(--secondary-red);
    }

    input[name="image"] {
        display: flex;
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
