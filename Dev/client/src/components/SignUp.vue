<script>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

const cupidURL = new URL('../assets/cupid_logo.png', import.meta.url).href

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


export default {
  name: 'SignUp'
};
</script>

<template>
    <div class="container">
        <img :src="'/get_img/'"  alt="Cupid Code Logo">
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
                <input type="image" :value="image" @change="(e) => image = e.target.value"/>
            </label>
            <label class="input_detail" for="address">
                Address
                <input type="text" :value="addr" @change="(e) => addr = e.target.value"/>
            </label>
            <div class="radios">
                Account Type
                <label class="input_detail" for="cupid">
                    Cupid
                    <input type="radio" id="cupid" name="accountType" :value="accType" />
                </label>
                <label class="input_detail" for="dater">
                    Dater
                    <input type="radio" id="dater" name="accountType" :value="accType" />
                </label>
            </div>

            <button class="button" @click="register">Create Account</button>
        </form>
    </div>
</template>

<style scoped>

</style>
