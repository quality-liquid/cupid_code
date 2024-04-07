<script setup>
    const props = defineProps(['gig'])
    function formatDateTime(datetimeString) {
        //Chat GPT with the tedious bs
        const date = new Date(datetimeString);
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const year = date.getFullYear() % 100; // Get last two digits of the year
        let hours = date.getHours();
        const minutes = ('0' + date.getMinutes()).slice(-2);
        const amPM = hours >= 12 ? 'PM' : 'AM';

        // Convert hours to 12-hour format
        hours = hours % 12 || 12;

        return `${month}/${day}/${year} ${hours}:${minutes} ${amPM}`;
    }
</script>
<template>
    <div>
        <h1 v-if="gig.cupid">Cupid: {{ gig.cupid }}</h1>
        <h2 v-else>Requested: {{ formatDateTime(gig.date_time_of_request) }}</h2>
        <p>Items requested: {{ gig.quest.items_requested }}</p>
        <p>Budget: ${{ gig.quest.budget }}</p>
        <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
    </div>
</template>
