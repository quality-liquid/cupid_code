<script setup>
</script>

<template>
    <div>
        <h1><!-- {{ gig.location }} --></h1>
        <p>Pickup: <!-- {{ gig.pickup }} --></p>
        <p>Deliver: <!-- {{ gig.deliver }} --></p>
        <p>Status: <!-- {{ gig.active ? 'Active' : 'Inactive' }} --></p>
    </div>
</template>

<style>
</style>