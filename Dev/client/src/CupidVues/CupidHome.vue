<script setup>
    import { makeRequest } from '../utils/make_request.js';
    import { ref, computed } from 'vue';

    
</script>

<template>
    <nav>
        Wow, a nav bar
    </nav>

    <div class="body">
        <!-- Clicking on this gig item, reroute to GigDetails page -->
        <div v-for="item in items" :key="item.id" 
        :class="{ 'active': item.active, 'inactive': !item.active }" 
        @click="">
            <h3>{{ item.location }}</h3>
            <p>Pickup: {{ item.Pickup }}</p>
            <p>Deliver Number: {{ item.Deliver }}</p>
            <p>Status: {{ item.active ? 'Active' : 'Inactive' }}</p>
            <button :class="{'active': !item.active, 'inactive': item.active}">
                {{ item.active ? 'Drop Gig' : 'Accept' }}
            </button>
        </div>
    </div>

</template>

<style scoped>
    .active {
      background-color: blue;
    }
    .inactive {
      background-color: red;
    }

    /* The side navigation menu */
    .sidenav {
        height: 100%; /* 100% Full-height */
        width: 0; /* 0 width - change this with JavaScript */
        position: fixed; /* Stay in place */
        z-index: 1; /* Stay on top */
        top: 0; /* Stay at the top */
        right: 0;
        background-color: #111; /* Black*/
        overflow-x: hidden; /* Disable horizontal scroll */
        padding-top: 60px; /* Place content 60px from the top */
        transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
    }

    /* The navigation menu links */
    .sidenav a {
        padding: 8px 8px 8px 32px;
        text-decoration: none;
        font-size: 25px;
        color: #818181;
        display: block;
        transition: 0.3s;
    }

    /* When you mouse over the navigation links, change their color */
    .sidenav a:hover {
        color: #f1f1f1;
    }

    /* Position and style the close button (top right corner) */
    .sidenav .closebtn {
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 36px;
        margin-left: 50px;
    }

    /* Style page content - use this if you want to push the page content to the right when you open the side navigation */
    #main {
        transition: margin-left .5s;
        padding: 20px;
    }

    /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
    @media screen and (max-height: 450px) {
        .sidenav {padding-top: 15px;}
        .sidenav a {font-size: 18px;}
    }
</style>