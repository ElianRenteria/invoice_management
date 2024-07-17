<template>
  <nav class="navbar">
    <InputText v-model="searchTerm" @input="onSearch" type="text" placeholder="Search Clients" />
    <Button label="Add" @click="onAddClient" severity="help" />
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
export default defineComponent({
  
  name: 'ClientsNavBar',
  components: {
    Button,
    InputText
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
      //this.$emit('addClient');
      this.$emit('toggleAddClientForm');
    }
  }
});
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  background-color: #f8f9fa;
  border-bottom: 1px solid #dee2e6;
}
</style>