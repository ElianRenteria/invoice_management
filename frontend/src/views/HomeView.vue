<template>
  <div class="home">
    <apiTest msg="Welcome to Your Vue.js + TypeScript App" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src

export default defineComponent({
  name: "HomeView",
  components: {
    apiTest,
  },
});
</script>
