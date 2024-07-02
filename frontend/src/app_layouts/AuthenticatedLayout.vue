<template>
    <div class="container">
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
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    width: 100%;
    height: 100%;
    padding: 0%;
    margin: 0%;
  }
</style>