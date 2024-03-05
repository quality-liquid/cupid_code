<script setup>
import {ref, computed} from 'vue';

const currPath = ref(window.location.hash)
const user = ref({})


window.addEventListener("hashchange", () => {
  currPath.value = window.location.hash
}) // This will run everytime it's changed to ensure it's correct.


</script>

<template>
  <h1> Hello, {{ user.firstname }}</h1>
</template>

<style scoped>

</style>