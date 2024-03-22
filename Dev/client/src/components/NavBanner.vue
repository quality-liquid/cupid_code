<!-- html render here 
      takes values
-->
<template id="topBanner">
  <nav>
    <figure @click="goBack" >{{ backIcon }}</figure>
    <figure>{{ searchIcon }}</figure>
    <figure @click="userAccount">{{ accountIcon }}</figure>
  </nav>
</template>





  <!-- variables + functions here -->
  <script>
    console.log("Header Started")
  
    const myVueComp = new Vue({
      el: "topBanner",
      data: {
        backIcon: "Back arrow",
        searchIcon: "magnifying glass",
        userInfo: "money/rating here",
        accountIcon: "account icon",
      },
      methods: {
        goBack(){
          // TODO: redirect to home page
        },
        userAccount(){
          // TODO: redirect to user account page
        },
        searchIcon(){
          // TODO: allow for search capability
        }
      },
    })
  
  </script>