<template>
    <div class="main">
      <Image :src="require('../assets/placeholder.png')" alt="Image" width="850" />
      <h1 class="title">Best <span class="highlight">Invoice Manager</span> for Contractors</h1>
      <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
      <Button label="Get Started" severity="info" class="main-button"/>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from "vue";
  import Knob from 'primevue/knob';
  import Image from 'primevue/image';
  import Button from 'primevue/button';
  
  export default defineComponent({
    name: "HomeView",
    components: {
      Image,
      Knob,
      Button
    },
  });
  </script>
  <style>
  .main {
    margin: auto;
    margin-top: 3%;
    width: 60%;
    padding: 5%;
    text-align: center;
  }
  .title {
    font-size: 4em;
  }
  
  .description {
    font-size: 1.2em;
  }
  
  .highlight {
    color: rgb(0,212,255);
    color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
  }
  
  .main-button {
    margin: 3%;
  }
  </style>