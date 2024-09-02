<template>
  <div>
    <h1>Clients</h1>
    <DataTable
      v-model:value="clients"
      v-model:filters="filters"
      v-model:selection="selectedClient"
      :selection-mode="'single'"
      data-key="id"
    >
      <template #header>
        <div class="flex justify-content-between">
          <template v-if="selectedClient">
            <div class="flex flex-row gap-3">
              <!-- Edit Button -->
              <Button
                label="Edit"
                icon="pi pi-pencil"
                @click="newClientDialogVisible = true"
              />
              <!-- Delete Button -->
              <Button
                label="Delete"
                icon="pi pi-trash"
                :severity="'danger'"
                @click=""
              />
            </div>
          </template>
          <template v-else>
            <!-- New Client Button -->
            <Button
              label="New Client"
              icon="pi pi-plus"
              outlined
              @click="newClientDialogVisible = true"
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
      <Column field="email" header="Email"></Column>
    </DataTable>
    <Dialog
      v-model="newClientDialogVisible"
      header="New Client"
      :maximizable="true"
      :modal="true"
      :visible="newClientDialogVisible"
      @update:visible="newClientDialogVisible = $event"
    >
      <ClientForm
        :client="selectedClient"
        @save="
          newClientDialogVisible = false;
          loadClients();
        "
      />
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { useClients } from "../../composables/useClients";
import { Client } from "../../types";
import { FilterMatchMode } from "primevue/api";
import { onKeyStroke } from "@vueuse/core";

const service = useClients();
const clients = ref<Client[]>([]);
const selectedClient = ref<Client | undefined>(undefined);
const newClientDialogVisible = ref(false);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const loadClients = () => {
  service.getClients().then((data) => {
    clients.value = data;
  });
};

onKeyStroke("Escape", () => {
  selectedClient.value = undefined;
});

onMounted(() => {
  loadClients();
});
</script>
