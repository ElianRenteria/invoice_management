<template>
  <div class="container">
    <component :is="layoutComponent" />
  </div>
</template>

<script>
import { computed } from "vue";
import { useRoute } from "vue-router";
import PublicLayout from "./app_layouts/PublicLayout.vue";
import AuthenticatedLayout from "./app_layouts/AuthenticatedLayout.vue";

export default {
  name: "App",
  components: {
    PublicLayout,
    AuthenticatedLayout,
  },
  setup() {
    const route = useRoute();
    const isAuthenticated = true;//!!localStorage.getItem("authToken");

    const layoutComponent = computed(() => {
      if (route.meta.requiresAuth && isAuthenticated) {
        return "AuthenticatedLayout";
      } else {
        return "PublicLayout";
      }
    });

    return {
      layoutComponent,
    };
  },
};
</script>

<style scoped>
  .container {
    width: 100%;
    height: 100%;
    padding: 0%;
    margin: 0%;
  }
  component {
    width: 100%;
    height: 100%;
    padding: 0%;
    margin: 0%;
  }
</style>

