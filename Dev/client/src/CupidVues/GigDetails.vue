<script setup>
    new Vue({
      el: '#app',
      data: {
        pickupComplete: false,
        itemsToPickup: [
          { id: 1, name: 'Item 1' },
          { id: 2, name: 'Item 2' },
          { id: 3, name: 'Item 3' }
        ],
        pickupLocation: 'Delivery Location'
      }
    });
</script>

<template>
    <!-- If a gig is active, background is blue. If inactive, background is red -->
    <div id="app" :class="{'active': gig.active, 'inactive': !gig.active}">
        <!-- gig.location is just the City and state -->
        <h1>Gig Details | <!-- {{ gig.location }} --></h1>
        <p>Pickup: <!-- {{ gig.pickup }} --></p>

        <!-- If a gig is active, show user info. If not active, don't show user info -->
        <div :class="{'show': gig.active, 'hidden': !gig.active}">
            <img src="" alt=""> <!-- Put picture of dater that submitted the gig here -->
            <label>
                <input type="checkbox" v-model="pickupComplete"> Pickup Complete
            </label>

            <p>Deliver: <!-- {{ gig.deliver }} --> </p>
            <p>Address: <!-- {{ gig.address }} This is the full street address --></p>

            <!-- If pickup is complete, show complete gig button -->
            <!-- If complete gig is clicked, reroute to GigComplete Page-->
            <button v-if="pickupComplete" @click="">Complete Gig</button> 
        </div>
    </div>
</template>

<style scoped>
    .show {
        display: block;
    }
    .hidden {
        display: none;
    }
    .active {
      background-color: blue;
    }
    .inactive {
      background-color: red;
    }
</style>