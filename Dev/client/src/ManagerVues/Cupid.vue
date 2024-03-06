<template>
  <!-- nav banner component -->
  <!-- end nav bar -->

  <figure>{{ cupidCount }} Cupids</figure>

  <!-- for loop for cupids -->
  <div v-for="cupid of cupids">
    <section>
      <nav>
        <figure>icon</figure>
        <p>{{ cupid.name }}</p>
      </nav>
      <article>
        <p>Rating: {{ cupid.rating }}</p>
        <p>Location: {{ cupid.location }}</p>
        <p>Completed Gigs: {{ cupid.completedGigs }}</p>
        <button>Suspend/Unsuspend</button>
      </article>      
    </section>
  </div>

</template>



<script setup>

  let cupids = ref([{ }])

  const cupidComponent = new VueElement({
    
    element: "#cupidStuffs",
    data: {
      name: "",
    },
    methods: {
      getCupidName(){
        this.name
      },
      getCupidRating() {
        this.rating
      },
      getCupidLocation(){
        this.location
      },
      getCupidCompletedGigs(){
        this.completedGigs
      }
    }
  })

</script>





<style>

</style>
  




