<template>
  <div class="sidebar">
    <Button icon="pi pi-times" @click="$emit('closeSidebar')" severity="help" rounded outlined />
    <h2>{{ client.name }}</h2>
    <div class="details">
      <div class="side">
        <p>{{ client.about }}</p>
        <p>{{ client.email }}</p>
        <p>{{ client.phone }}</p>
      </div>
      <div class="side">
        <p>{{ client.address }}</p>
        <p>{{ client.city }}</p>
        <p>{{ client.state }}</p> 
        <p>{{ client.zip }}</p> 
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from 'primevue/button';
  export default defineComponent ({
    name: 'ClientDetailSidebar',
    props: ['client'],
    components: {
      Button
    }
  });
</script>

<style scoped>
  .sidebar {
    width: 50%;
    padding: 20px;
    background-color: #ffffff;
    box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
    border: 1px solid #dee2e6;
  }

  .details {
    display: flex;
    justify-content: space-around;
  }
</style>