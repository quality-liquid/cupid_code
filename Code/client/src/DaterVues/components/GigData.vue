<script setup>
    const props = defineProps(['gig'])
</script>
<template>
    <div>
        <h1 v-if="gig.cupid">Cupid: {{ gig.cupid }}</h1>
        <h1 v-else>Requested: {{ gig.date_time_of_request }}</h1>
        <p>Items requested: {{ gig.quest.items_requested }}</p>
        <p>Budget: ${{ gig.quest.budget }}</p>
        <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
    </div>
</template>
