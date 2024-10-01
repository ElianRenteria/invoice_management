<template>
  <div>
    <h1>Services</h1>
    <DataTable
      v-model:value="services"
      v-model:filters="filters"
      v-model:selection="selectedService"
      :selection-mode="'single'"
      data-key="id"
      sortField="price"
      :sortOrder="1"
      :paginator="true"
      :rows="10"
      :rows-per-page-options="[5, 10, 25, 50, 100]"
    >
      <template #header>
        <div class="flex justify-content-between">
          <template v-if="selectedService">
            <div class="flex flex-row gap-3">
              <!-- Edit Button -->
              <Button
                label="Edit"
                icon="pi pi-pencil"
                @click="newServiceDialogVisible = true"
              />
              <!-- Delete Button -->
              <Button
                label="Delete"
                icon="pi pi-trash"
                :severity="'danger'"
                @click="deleteService(selectedService)"
              />
            </div>
          </template>
          <template v-else>
            <!-- New Service Button -->
            <Button
              label="New Service"
              icon="pi pi-plus"
              outlined
              @click="newServiceDialogVisible = true"
            />
          </template>
          <!-- Filter Input Field -->

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
    <Dialog
      v-model="newServiceDialogVisible"
      :header="selectedService ? 'Edit Service' : 'New Service'"
      :maximizable="false"
      :modal="true"
      :visible="newServiceDialogVisible"
      @update:visible="newServiceDialogVisible = $event"
    >
      <ServiceForm
        :service="selectedService"
        @save="
          newServiceDialogVisible = false;
          selectedService = undefined;
          loadServices();
        "
      />
    </Dialog>
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
import { onKeyStroke } from "@vueuse/core";

const service = useServices();
const services = ref<Service[]>([]);
const selectedService = ref<Service | undefined>(undefined);
const newServiceDialogVisible = ref(false);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const deleteService = (chosenService: Service) => {
  service.deleteService(chosenService).then(() => {
    loadServices();
    selectedService.value = undefined;
  });
};

const loadServices = () => {
  service.getServices().then((data) => {
    services.value = data;
  });
};

onKeyStroke("Escape", () => {
  selectedService.value = undefined;
});

onMounted(() => {
  loadServices();
});
</script>

<style scoped></style>
