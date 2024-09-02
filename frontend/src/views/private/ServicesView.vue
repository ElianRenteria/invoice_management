<template>
  <div>
    <h1>Services</h1>
    <DataTable
      v-model:value="services"
      v-model:filters="filters"
      data-key="id"
      sortField="price"
      :sortOrder="1"
      :paginator="true"
      :rows="10"
      :rows-per-page-options="[5, 10, 25, 50, 100]"
    >
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
      <Column field="price" header="Price" sortable>
        <template #body="{ data }">
          {{ formatCurrency(data.price) }}
        </template>
      </Column>
    </DataTable>
    <p class="text-center text-color-secondary">
      Total Results: {{ services.length }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { useServices } from "../../composables/useServices";
import { Service } from "../../types/Service";
import { FilterMatchMode } from "primevue/api";
import { formatCurrency } from "../../utils/formatters";
const service = useServices();
const services = ref<Service[]>([]);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
onMounted(async () => {
  services.value = await service.getServices();
});
</script>

<style scoped></style>
