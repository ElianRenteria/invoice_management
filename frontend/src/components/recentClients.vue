<template>
    <div class="w-full h-auto container pt-3 pb-3 pr-6">
      <div class=" graphs w-full h-full container p-3">
        <h1>Recent Clients</h1>
      </div>
    </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  
  export default defineComponent({
    name: "recentClients",
  });
</script>

<style scoped>
    .graphs {
        background-color: #211641;
        border-radius: 1rem;
    }
</style>