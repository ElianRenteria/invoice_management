<template>
    <div class="flex flex-row justify-content-center align-items-start h-full ">
      <SidePanelNav />
      <router-view />
    </div>
  </template>
  
  <script>
  import SidePanelNav from "../components/SidePanelNav.vue";
  export default {
    name: "AuthenticatedLayout",
    components: {
      SidePanelNav,
    },
  };
  </script>
