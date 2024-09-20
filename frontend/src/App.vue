<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style scoped></style>

<script setup lang="ts">
// import PrivateLayout from "./layouts/PrivateLayout.vue";
// import PublicLayout from "./layouts/PublicLayout.vue";
import { useRoute } from "vue-router";

const route = useRoute();
const layout = computed(() => {
  console.log(route);
  console.log(route.meta.internalLayout);
  return route.meta.internalLayout ? "PrivateLayout" : "PublicLayout";
});
</script>
