<template>
  <!-- Name, Company Name, and Primary Contact Name -->
  <div class="flex flex-row gap-3 my-3">
    <div class="flex flex-column gap-2">
      <label for="name">Name</label>
      <InputText id="name" v-model="client.name" />
      <label for="name" class="text-xs text-color-secondary">
        Full name of the client or company
      </label>
    </div>
    <div class="flex flex-column gap-2">
      <label for="name">Company Name</label>
      <InputText id="name" v-model="client.company_name" />
      <label for="name" class="text-xs text-color-secondary">
        Company name, if applicable
      </label>
    </div>
    <div class="flex flex-column gap-2">
      <label for="email">Primary Contact</label>
      <InputText id="email" v-model="client.email" />
      <label for="name" class="text-xs text-color-secondary">
        Name of the primary contact person for the client
      </label>
    </div>
  </div>
  <!-- Status, Industry, and Website -->
  <div class="flex flex-row gap-3 my-3">
    <div class="flex flex-column gap-2">
      <label for="status">Status</label>
      <Dropdown
        id="status"
        v-model="client.status"
        :options="clientStatusOptions"
        optionLabel="label"
        optionValue="value"
        placeholder="Select a Status"
      />
    </div>
    <div class="flex flex-column gap-2">
      <label for="industry">Industry</label>
      <Dropdown
        id="industry"
        v-model="client.industry"
        :options="[]"
        optionLabel="name"
        optionValue="value"
        placeholder="Select an Industry"
      />
    </div>
    <div class="flex flex-column gap-2">
      <label for="website">Website</label>
      <InputText id="website" v-model="client.website" />
    </div>
  </div>
  <!-- Phone, Fax, and Email -->
  <div class="flex flex-row gap-3 my-3">
    <div class="flex flex-column gap-2">
      <label for="phone">Phone</label>
      <InputText id="phone" v-model="client.phone" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="facsimile">Fax</label>
      <InputText id="fascimile" v-model="client.facsimile" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="email">Email</label>
      <InputText id="email" v-model="client.email" />
    </div>
  </div>
  <div class="p-fluid mt-3">
    <Button
      :label="editMode ? 'Update' : 'Save'"
      :icon="editMode ? 'pi pi-pencil' : 'pi pi-save'"
      class="flex-grow"
      @click="saveClient"
    />
  </div>
</template>

<script setup lang="ts">
import { Client, clientStatusOptions } from "../../types";
import { useClients } from "../../composables/useClients";
import { initializeClient } from "../../utils/initialize";
import { watchImmediate } from "@vueuse/core";

// Import the createClient function from the composable
const { createClient } = useClients();

// Define props with default value
const props = defineProps({
  client: {
    type: Object as PropType<Client>,
    default: initializeClient(),
  },
});

// Use a reactive reference for client state management
const client = ref<Client>(props.client);

// Define emits
const emits = defineEmits(["save"]);

// Define computed properties
const editMode = computed(() => !!props.client?.id);

// Watch for changes in the prop and reset if unassigned
watchImmediate(props, (updated) => {
  if (!updated.client) {
    client.value = initializeClient();
  } else {
    client.value = updated.client;
  }
});

const saveClient = async () => {
  if (editMode.value) {
    // Update Client
    // await updateClient(props.client);
  } else {
    // Create Client
    await createClient(props.client);
  }
  emits("save");
};
</script>
