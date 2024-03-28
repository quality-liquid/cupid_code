<script setup>
// NOTE: I tried matching the results names to what I can see in the views.py and helper.py 
//If things are reading null or undefined, just console.log(results) to see what the names are and then change `results.data` to `results.<foundName>`
import {ref, onMounted} from 'vue'
import { makeRequest } from '../utils/make_request';

const daters = ref(0) //Fill with a setter type for whatever the backend returns to you 
const cupids = ref(0)
const active_cupids = ref(0)
const active_daters = ref(0)

async function getDatersTotal() {
  const results = await makeRequest('/api/manager/dater_count')
  daters.value = results.data
}

async function getCupidsTotal() {
  const results = await makeRequest('/api/manager/cupid_count')
  cupids.value = results.data
}

async function getCurrActiveTotal() {
  const cupid_res = await makeRequest('/api/manager/active_cupids')
  active_cupids.value = cupid_res.data 
  const dater_res= await makeRequest('/api/manager/active_daters/')
  active_daters.value = dater_res.data
}

onMounted(getCupidsTotal)
onMounted(getDatersTotal)
onMounted(getCurrActiveTotal)
</script>

<template>
  <!-- nav banner component -->
  <!--  -->

  <article>Daters</article>
  <article>Cupids</article>

  <figure>Graph</figure>

  <figure>{{ daters }} Users</figure>
  <figure>{{ cupids }} Cupids stats</figure>
  <figure>{{ active_cupids }} Active Cupids</figure>
  <figure>{{ active_daters }} Active Daters</figure>
  <figure>Other Info</figure>

</template>

<style scoped>

</style>
  




