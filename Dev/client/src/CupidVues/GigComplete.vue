<script setup>
</script>

<template>
    <nav></nav>

    <h1>Gig Complete! </h1>
    <form action="">
        <h3>Would you like to rate your dater? </h3>
        <div class="radios">
            <input type="radio">
            <label for="yes">Yes</label>

            <input type="radio">
            <label for="no">No</label>
        </div>        

        <div>
            <label for="daterRating"> How would you rate the dater you serviced? (between 0 and 5):</label>
            <input type="range" id="daterRating" name="daterRating" min="0" max="5">
        </div>

        <div>
            <label for="comments">Any issues or complements you would like to include? </label>
            <input type="text">
        </div>
    </form>
</template>

<style scoped>
</style>