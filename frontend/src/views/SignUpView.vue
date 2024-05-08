<template>
  <div class="main">
    <h1>Sign Up Page</h1>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  
  export default defineComponent({
    name: "LoginView",
    components: {
      apiTest,
    },
  });
</script>
  