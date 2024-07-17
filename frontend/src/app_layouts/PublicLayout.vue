<template>
    <div class="container">
      <NavBar />
      <router-view />
    </div>
</template>

<script setup lang="ts">
  import NavBar from "../components/NavBar.vue";
</script>
<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    padding: 0%;
    margin: 0%;
  }
</style>
  