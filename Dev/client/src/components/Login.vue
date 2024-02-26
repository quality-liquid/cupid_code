<script>
import { makeRequest } from '../utils/make_request.js';
import cupid_logo from '../assets/cupid_logo.png'

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
    <div id="login_paper">
        <img :src="cupid_logo" alt="Cupid Code Logo">
        <form action={{ login() }}>
            <div>
                <label class="form_input">
                Email
                <input type="email" name="email">
                </label>
            </div>
            <div class="">
                <label class="form_input">
                Password
                <input type="password" name="password">
                </label>
            </div>
            <button class="big_button">Sign In</button>
        </form>

        <a href="/register">Create Account</a>
    </div>
</template>

<style scoped>
    body {
        background-color: #5675FF;
        place-items: center;
    }
    
    .big_button {
        background-color: #ff6ba2;
        border-radius: 10px;
    }
</style>
