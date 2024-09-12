<template>
    <div>
      <h1>Invoices</h1>
      <DataTable
        v-model:value="invoices"
        v-model:filters="filters"
        v-model:selection="selectedInvoice"
        :selection-mode="'single'"
        data-key="id"
        :paginator="true"
        :rows="10"
        :rows-per-page-options="[5, 10, 25, 50, 100]"
      >
        <template #header>
          <div class="flex justify-content-between">
            <template v-if="selectedInvoice">
              <div class="flex flex-row gap-3">
                <!-- Edit Button -->
                <Button
                  label="Edit"
                  icon="pi pi-pencil"
                  @click="newInvoiceDialogVisible = true"
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
              <!-- New Invoice Button -->
              <Button
                label="New Invoice"
                icon="pi pi-plus"
                outlined
                @click="newInvoiceDialogVisible = true"
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
        v-model="newInvoiceDialogVisible"
        header="New Invoice"
        :maximizable="true"
        :modal="true"
        :visible="newInvoiceDialogVisible"
        @update:visible="newInvoiceDialogVisible = $event"
      >
        <InvoiceForm
          :invoice="selectedInvoice"
          @save="
            newInvoiceDialogVisible = false;
            loadInvoices();
          "
        />
      </Dialog>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useInvoices } from "../../composables/useInvoices";
  import { Invoice } from "../../types";
  import { FilterMatchMode } from "primevue/api";
  import { onKeyStroke } from "@vueuse/core";
  
  const service = useInvoices();
  const invoices = ref<Invoice[]>([]);
  const selectedInvoice = ref<Invoice | undefined>(undefined);
  const newInvoiceDialogVisible = ref(false);
  
  const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });
  
  const loadInvoices = () => {
    service.getInvoices().then((data) => {
      invoices.value = data;
    });
  };
  
  onKeyStroke("Escape", () => {
    selectedInvoice.value = undefined;
  });
  
  onMounted(() => {
    loadInvoices();
  });
  </script>