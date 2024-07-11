<template>
    <div class="w-full h-full container pt-2 pb-2 px-6">
      <div class=" graphs w-full h-full container p-3">
        <h1>invoices</h1>
      </div>
    </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  
  export default defineComponent({
    name: "invoices",
  });
</script>

<style scoped>
    .graphs {
        background-color: #211641;
        border-radius: 1rem;
    }
</style>