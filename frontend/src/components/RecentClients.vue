<template>
  <div class="invoice-container">
    <div class="header">
      <h2>Recent Clients</h2>
    </div>
    <div class="client-holder">
      <Listbox v-model="selectedClient" :options="clients" filter optionLabel="name" class="w-full md:w-56" listStyle="max-height:200px"/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Listbox from 'primevue/listbox';

export default defineComponent({
  name: 'RecentClients',
  components: {
    Listbox,
  },
  data() {
    return {
      selectedClient: null,
      clients: [
        { name: 'John Doe' },
        { name: 'Joseph Stalin' },
        { name: 'Peter Griffin' },
        { name: 'Eric Cartman' },
        { name: 'Kyle Broflofski' },
      ]
    }
  },
});
</script>

<style scoped>

.invoice-container {
  width: 15%;
  padding: 1%;
  box-sizing: border-box;
  background-color: rgba(176, 107, 255, 0.3);
  margin: 1%;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-bottom: 10px;
}

.client-holder {
  overflow-y: auto;
}

</style>