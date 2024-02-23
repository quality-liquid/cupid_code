<script setup>
</script>

<template>
    <div>
        <img src="../assets/cupid_logo.png" alt="Cupid Code Logo">
        <h1>Create Your Account!</h1>
        <form action="/registration/sign_in/">
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

        <a href="Sign Up">Create Account</a>
    </div>
</template>

<style scoped>

</style>
