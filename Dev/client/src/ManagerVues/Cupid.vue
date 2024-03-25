<template>
  <!-- nav banner component -->
  <!-- end nav bar -->

  <figure>{{ cupidCount }} Cupids</figure>

  <!-- for loop for cupids -->
  <div v-for="cupid of cupids">
    <section>
      <nav>
        <figure>icon</figure>
        <p>{{ cupid.user.first_name }}</p>
      </nav>
      <article>
        <p>Rating: {{ cupid.rating_sum }}</p>
        <p>Location: {{ cupid.location }}</p>
        <p>Completed Gigs: {{ cupid.completed_gigs }}</p>
        <button>Suspend/Unsuspend</button>
      </article>      
    </section>
  </div>

</template>



<script setup>
import { ref, onMounted } from 'vue';
import { makeRequest } from '../utils/make_request';

const cupids = ref([{ }])
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

async function getCupids() {
  const res = await makeRequest('/api/manager/cupids')
  cupids.value = res.cuipds
}

</script>





<style>

</style>
  




