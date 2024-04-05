<script setup>
import router from '../router'

</script>

<template>
<div class="container">
    You are Suspended and cannot access your account.<br>
    For more information, or to get unsuspended, please email us at <br>
    <a>support@cupidcode.com</a>
</div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    color: black;
    margin: 10px;
    margin-top: 50px;
}

.container a {
    color: var(--primary-blue);
}
</style>