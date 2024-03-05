<template>
  <!-- nav banner component -->
  <!-- end nav bar -->

  <figure>{{ daterCount }} Daters</figure>

  <!-- for loop for daters -->
  <div v-for="dater of daters">
    <section>
      <nav >{{ dater.name }}</nav>
      <article>
        <p>Rating: {{ dater.rating }}</p>
        <p>Location: {{ dater.location }}</p>
        <p>Completed Gigs: {{ dater.completedGigs }}</p>
        <button>Suspend/Unsuspend</button>
      </article>      
    </section>
  </div>

</template>



<script setup>

  let daters = ref([{ }])

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

</script>





<style>

</style>
  




