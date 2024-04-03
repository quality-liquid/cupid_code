<script setup>
    const props = defineProps(['gig'])
</script>
<template>
    <div>
        <h1>Dater: {{ gig.dater }}</h1>
        <p>Items requested: {{ gig.quest.items_requested }}</p>
        <p>Budget: ${{ gig.quest.budget }}</p>
        <p>Pickup Location: {{ gig.quest.pickup_location }}</p>
    </div>
</template>
