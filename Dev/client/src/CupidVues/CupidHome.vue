<script setup>
    /* Set the width of the side navigation to 250px */
    function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
    }

    /* Set the width of the side navigation to 0 */
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
    }

    /* Pretty sure this is how data is made available to be displayed in the template tag */
    new Vue({
      el: '#app',
      router,
      data: {
        gigs: [
          { id:"0", location: 'Logan UT', pickup: 'Wow, a description!', deliver: '123 Street Drive, Logan UT', active: true },
          { id:"1", location: 'Logan UT', pickup: 'Wow, a description!', deliver: '123 Street Drive, Logan UT', active: false },
          { id:"2", location: 'Somewhere UT', pickup: 'Wow, a description!', deliver: '123 Street Drive, Somewhere UT', active: true }
        ]
      }, 
      methods: {
        viewGig(gig) {
            this.$router.push({ path: `/gig/${gig.id}`, params: { gig } });
        }
      }
    });

    const GigInfo = {
      template: `
        <div>
          <h1>{{ gig.location }}</h1>
          <p>Email: {{ gig.pickup }}</p>
          <p>Phone Number: {{ gig.deliver }}</p>
          <p>Status: {{ gig.active ? 'Active' : 'Inactive' }}</p>
          <button @click="goBack">Go Back</button>
        </div>
      `,
      data() {
        return {
          gig: {}
        };
      },
      methods: {
        goBack() {
          this.$router.go(-1);
        }
      },
      created() {
        this.gig = this.$route.params.gig;
      }
    };

    const routes = [
      { path: '/gig/:id', component: GigInfo, props: true }
    ];

    const router = new VueRouter({
      routes
    });
</script>

<template>
    <nav>
        <span>Rating: </span> 
        <!-- TODO: Put their rating here! -->
        
        <div id="accountPopOut" class="sidnav">
            <a href="">Logout</a>
        </div>

        <span onclick="openNav()">
            <img src="" alt="">
            <!-- Basic user picture goes here!  -->
        </span>
    </nav>

    <div class="body">
        <div v-for="item in items" :key="item.id" 
        :class="{ 'active': item.active, 'inactive': !item.active }" 
        @click="viewGig(item)">
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