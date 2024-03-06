<template>
  <!-- nav banner component -->
  <!--  -->

  <article>Daters</article>
  <article>Cupids</article>

  <figure>Graph</figure>

  <figure>{{ daters.total }} Users</figure>
  <figure>{{ cupids.total }} Cupids stats</figure>
  <figure>{{ cupids.currActiveTotal }} Active Cupids</figure>
  <figure>Other Info</figure>

</template>

<script setup>
  const managerComponent = new VueElement({
    el: "#managerPage",
    data: {

    },
    methods: {
      getDatersTotal(){
        daters.total
      },
      getCupidsTotal(){
        cupids.total
      },
      getCurrActiveTotal(){
        cupids.currActive
      }
    }
  })
</script>





<style>

</style>
  




