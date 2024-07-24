<template>
  <div class="main">
    <h1 class="main-title">About <span class="highlight">Us</span></h1>
  </div>

  <div class="content">
    <Fieldset legend="Who are we ?">
      <p class="m-0 about-text">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </Fieldset>
    <br>
    <Fieldset legend="Our mission"  style="text-align: center;">
      <p class="m-0 about-text" style="text-align: left;">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </Fieldset>
    <br>
    <Fieldset legend="Our values" style="text-align: right;">
      <p class="m-0 about-text" style="text-align: left;">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </Fieldset>
  </div>
  <Footer />
</template>
<script lang="ts">
  import Fieldset from 'primevue/fieldset';
  import Footer from '@/components/Footer.vue';
  import { defineComponent } from "vue";
  export default defineComponent({
    name: "AboutView",
    components: {
      Fieldset,
      Footer
    },
  })
</script>
<style scoped>
  .content {
    margin: 0% 20%;
    margin-bottom: 5%;
  }

  .about-text {
    font-size: 1.3em;
  }

  .main {
    margin: 3%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 8% 27%;
  }

  .main-title {
    font-size: 4em;
    text-align: center;
  }

  .highlight {
    color: rgb(0,212,255);
    color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
  }
</style>