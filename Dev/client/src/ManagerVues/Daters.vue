<template>
  <!-- nav banner component -->
  <!-- end nav bar -->

  <figure>{{ daterCount }} Daters</figure>

  <!-- for loop for daters -->
  <div v-for="dater of daters">
    <section class="userListItem">
      <nav>
        <figure>icon</figure>
        <p>{{ dater.user.first_name }}</p>
      </nav>
      <article>
        <p>Rating: {{ dater.rating_sum }}</p>
        <p>Location: {{ dater.location }}</p>
        <p>Completed Gigs: {{ dater.completed_gigs }}</p>
        <button>Suspend/Unsuspend</button>
      </article>      
    </section>
  </div>

</template>



<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

const daters = ref([{ }])
/*
Bad syntax. These 
const daterComponent = new VueElement({
  
  element: "#daterstuffs",
  data: {
    name: "",
  },
  methods: {
    getDaterName(){
      this.name
    },
    getDaterRating() {
      this.rating
    },
    getDaterLocation(){
      this.location
    },
    getDaterTotalDates(){
      this.totalDates
    }
  }
})
*/

async function getDaters() {
  const res = await makeRequest('/api/manager/daters')
  daters.value = res.daters
}
  

</script>





<style>

</style>
  




