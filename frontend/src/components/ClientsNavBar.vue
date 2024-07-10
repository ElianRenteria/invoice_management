<template>
  <nav class="navbar">
    <input type="text" v-model="searchTerm" @input="onSearch" placeholder="Search clients..." />
    <Button label="Search" @click="onSearch" />
    <Button label="Add" @click="onAddClient" />
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from 'primevue/button';
export default defineComponent({
  
  name: 'ClientsNavBar',
  components: {
    Button
  },
  data() {
    return {
      searchTerm: ''
    };
  },
  methods: {
    onSearch() {
      this.$emit('search', this.searchTerm);
    },
    onAddClient() {
      this.$emit('addClient');
    }
  }
});
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background-color: #f8f9fa;
  border-bottom: 1px solid #dee2e6;
}
</style>