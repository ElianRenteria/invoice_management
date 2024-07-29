<template>
  <div>
    <h1>Clients</h1>
    <DataTable v-model:value="clients" v-model:filters="filters" data-key="id">
      <template #header>
        <div class="flex justify-content-end">
          <IconField iconPosition="left">
            <InputIcon>
              <i class="pi pi-search" />
            </InputIcon>
            <InputText
              v-model="filters['global'].value"
              placeholder="Keyword Search"
            />
          </IconField>
        </div>
      </template>
      <Column field="name" header="Name"></Column>
      <Column field="email" header="Email"></Column>
    </DataTable>
  </div>
</template>

<script setup lang="ts">
import { useClients } from "../../composables/useClients";
import { Client } from "../../types";
import { FilterMatchMode } from "primevue/api";

const service = useClients();
const clients = ref<Client[]>([]);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
onMounted(async () => {
  clients.value = await service.getClients();
});
</script>
