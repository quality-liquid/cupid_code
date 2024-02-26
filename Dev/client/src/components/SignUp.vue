<script>
import { makeRequest } from '../utils/make_request.js';

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
        <img src="../assets/cupid_logo.png" alt="Cupid Code Logo">
        <h1>Create Your Account!</h1>
        <form action={{ register() }}>
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
