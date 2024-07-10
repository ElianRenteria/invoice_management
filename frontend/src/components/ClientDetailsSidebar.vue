<template>
  <div class="sidebar">
    <button @click="$emit('closeSidebar')">Close</button>
    <h2>{{ client.name }}</h2>
    <p>{{ client.details }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
  export default defineComponent ({
    name: 'ClientDetailSidebar',
    props: ['client']
  });
</script>

<style>
  .sidebar {
    width: 300px;
    padding: 20px;
    background-color: #ffffff;
    box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
  }
</style>