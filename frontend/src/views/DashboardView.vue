<template>
    <div class="container">
      <SearchBarHeader />
      <dataVisualization />
      <div class="recents flex flex-row justify-content-evenly align-content-center w-full h-full">
        <recentInvoices />
        <recentClients />
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import SearchBarHeader from "@/components/SearchBarHeader.vue";
  import dataVisualization from "@/components/dataVisualization.vue";
  import recentClients from "@/components/recentClients.vue";
  import recentInvoices from "@/components/recentInvoices.vue";
  
  export default {
    components: {
      SearchBarHeader,
      dataVisualization,
      recentClients,
      recentInvoices
    }
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #140a2c;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 100%;
    padding: 0%;
    margin: 0%;
  }
  </style>
  