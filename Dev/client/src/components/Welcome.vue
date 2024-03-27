<script setup>
import router from '../router';
</script>

<template>
  <div class="image">
    <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
  </div>
  <div class="container">
        Welcome to Cupid Code, where love meets technology in the most nerdy and delightful way possible! <br>
        Are you tired of awkward dates and missed opportunities? Look no further! Cupid Code is here to revolutionize your dating experience. <br>
        <br>
        Our AI-powered app is designed specifically for the more intellectually inclined, offering a plethora of 
        features to ensure your romantic endeavors are nothing short of spectacular. <br>
        Engage in witty banter and receive invaluable dating advice through our chatting feature, where our AI companion is always ready to lend a helping hand (or line). <br>
        <br>
        Worried about those nerve-wracking moments during your date? Activate our listening feature and let the AI discreetly guide you towards success. <br>
        Keep your love life organized with our handy calendar feature, ensuring you never miss a chance to charm that special someone. <br>
        And with our built-in transaction system, you can set a budget for the AI to use in securing goods and services, ensuring your date goes off without a hitch.<br>
        <br>
        Say goodbye to dating woes and hello to a world of endless possibilities with Cupid Code. Whether you're a seasoned romantic or a first-time dater, <br>
        let us help you crack the code to finding love in the digital age. Welcome to your new favorite wingman!
  </div>
  <div class="container">
    <router-link to="#/register">Get Started Now!</router-link>
  </div>

</template>

<style scoped>
  .image {
    display: flex;
    justify-content: center;
    margin-top: 50px;
    border-radius: 16px;
  }
  .container {
    display: flex;
    justify-content: center;
    margin-top: 30px;
    padding: 10px;
  }
</style>