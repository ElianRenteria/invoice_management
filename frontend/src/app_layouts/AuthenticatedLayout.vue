<template>
    <div class="flex flex-row justify-content-center align-items-start h-full ">
      <SidePanelNav />
      <router-view />
    </div>
  </template>
  
  <script setup lang="ts">
    import SidePanelNav from "../components/SidePanelNav.vue";
  </script>
