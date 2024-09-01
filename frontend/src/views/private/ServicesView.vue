<template>
    <div>
        <h1>Services</h1>
        <DataTable v-model:value="services" v-model:filters="filters" data-key="id">
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
            <Column field="price" header="Price"></Column>
        </DataTable>
    </div>
</template>
  
<script setup lang="ts">
  import { useServices } from "../../composables/useServices";
  import { Service } from "../../types/Service";
  import { FilterMatchMode } from "primevue/api";
  import CurrencyFormatter from "../../utils/currencyFormatter";
  const service = useServices();
  const services = ref<Service[]>([]);
  
  const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });
  onMounted(async () => {
    services.value = await service.getServices();
    services.value.forEach((obj) => {
        obj.price = CurrencyFormatter.format(obj.price);
    })
});
</script>

<style scoped>
  

</style>
