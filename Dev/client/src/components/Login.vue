<script setup>
</script>

<template>
    <div id="login_paper">
        <img src="../assets/cupid_logo.png" alt="Cupid Code Logo">
        <form action="/registration/sign_in/">
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

        <a href="Sign Up">Create Account</a>
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
