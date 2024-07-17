<template>
  <div class="client-list">
    <ul>
      <li v-for="client in clients" :key="client.id" @click="selectClient(client)">
        {{ client.name }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
  export default defineComponent ({
    name: 'ClientList',
    props: ['clients'],
    methods: {
      selectClient(client: string) {
        this.$emit('selectClient', client);
      }
    }
  });
</script>

<style scoped>
  .client-list {
    width: 50%;
    border: 1px solid #dee2e6;
  }

  .client-list ul {
    list-style-type: none;
    padding: 0;
  }

  .client-list li {
    padding: 10px;
    cursor: pointer;
  }

  .client-list li:hover {
    background-color: #f1f1f1;
  }
</style>