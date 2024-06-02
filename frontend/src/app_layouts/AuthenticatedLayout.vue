<template>
    <div>
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
  