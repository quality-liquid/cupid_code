<script>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

const cupidURL = new URL('../assets/cupid_logo.png', import.meta.url).href

const email = ref('')
const password = ref('')
const accType = ref('')



async function register() {
    // Validate data 
    await makeRequest('/sign_in/', 'post', {
        email,
        password,
        accountType,

    })
    // Redirect to dashboard
}


export default {
  name: 'SignUp'
};
</script>

<template>
    <div>
        <img :src="cupidURL" alt="Cupid Code Logo">
        <h1>Create Your Account!</h1>
        <form>
            <label>
                Email
                <input type="email" />
            </label>
            <label class="form_input">
                Account Type
                <br>
                
                <input type="radio" id="cupid" name="accountType" value="Cupid">
                <label for="cupid">Cupid</label>
                <input type="radio" id="dater" name="accountType" value="Cupid">
                <label for="dater">Dater</label>
                
                <br>
                <button>Create Account</button>
            </label>
        </form>
    </div>
</template>

<style scoped>

</style>
