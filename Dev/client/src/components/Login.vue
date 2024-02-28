<script>
import { makeRequest } from '../utils/make_request.js';

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
        <img :src="'localhost:5173/static/assets/cupid_code.png'" alt="Cupid Code Logo">
        <form>
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
            <button class="big_button" @click="login">Sign In</button>
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
