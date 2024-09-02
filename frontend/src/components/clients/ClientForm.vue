<template>
  <!-- Name, Company Name, and Primary Contact Name -->
  <div class="flex flex-row gap-3 py-3">
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
  <div class="flex flex-row gap-3">
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
        :options="industryOptions"
        :filter="true"
        :showClear="true"
        placeholder="Select an Industry"
      >
        <template #value="option">
          <div class="flex flex-row align-items-center gap-2">
            <span>{{ option.value || "Select Industry" }}</span>
          </div>
        </template>
      </Dropdown>
    </div>
    <div class="flex flex-column flex-grow-1 gap-2">
      <label for="website">Website</label>
      <InputText id="website" v-model="client.website" />
    </div>
  </div>
  <!-- Phone, Fax, and Email -->
  <Divider />
  <div class="py-3">
    <span class="text-lg font-semibold text-color-primary"> Contact </span>
  </div>
  <div class="flex flex-row gap-3 pb-3">
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
  <Divider />
  <!-- Billing Address -->
  <div class="py-3">
    <span class="text-lg font-semibold text-color-primary">
      Billing Address
    </span>
  </div>
  <div class="flex flex-row gap-3 pb-3">
    <div class="flex flex-column gap-2">
      <label for="address_line1">Street Address</label>
      <InputText id="address_line1" v-model="client.billing_address_line1" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_line2">Suite, Unit, Building</label>
      <InputText id="address_line2" v-model="client.billing_address_line2" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_city">City</label>
      <InputText id="address_city" v-model="client.billing_address_city" />
    </div>
  </div>
  <div class="flex flex-row gap-3 pb-3">
    <div class="flex flex-column gap-2">
      <label for="address_state">State</label>
      <InputText id="address_state" v-model="client.billing_address_state" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_postal_code">Postal Code</label>
      <InputText
        id="address_postal_code"
        v-model="client.billing_address_postal_code"
      />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_country">Country</label>
      <InputText id="address_city" v-model="client.billing_address_country" />
    </div>
  </div>
  <Divider />
  <!-- Mailing Address -->
  <div class="flex flex-row justify-content-between align-items-center py-3">
    <span class="text-lg font-semibold text-color-primary">
      Mailing Address
    </span>
    <Button
      :size="'small'"
      :label="'Copy Billing Address'"
      :severity="'secondary'"
      @click="copyBillingAddress"
    />
  </div>
  <div class="flex flex-row gap-3 pb-3">
    <div class="flex flex-column gap-2">
      <label for="address_line1">Street Address</label>
      <InputText id="address_line1" v-model="client.address_line1" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_line2">Suite, Unit, Building</label>
      <InputText id="address_line2" v-model="client.address_line2" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_city">City</label>
      <InputText id="address_city" v-model="client.address_city" />
    </div>
  </div>
  <div class="flex flex-row gap-3 pb-3">
    <div class="flex flex-column gap-2">
      <label for="address_state">State</label>
      <InputText id="address_state" v-model="client.address_state" />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_postal_code">Postal Code</label>
      <InputText
        id="address_postal_code"
        v-model="client.address_postal_code"
      />
    </div>
    <div class="flex flex-column gap-2">
      <label for="address_country">Country</label>
      <InputText id="address_city" v-model="client.address_country" />
    </div>
  </div>
  <Divider />
  <!-- Notes -->
  <div class="py-3">
    <span class="text-lg font-semibold text-color-primary"> Notes </span>
  </div>
  <div class="flex flex-row gap-3 pb-3">
    <div class="flex flex-column flex-grow-1 gap-2">
      <label for="notes">Notes</label>
      <Textarea id="notes" v-model="client.notes" :autoResize="true" />
    </div>
  </div>
  <!-- Save Button -->
  <div class="p-fluid pt-4">
    <Button
      :label="editMode ? 'Update' : 'Save'"
      :icon="editMode ? 'pi pi-pencil' : 'pi pi-save'"
      class="flex-grow"
      @click="saveClient"
    />
  </div>
</template>

<script setup lang="ts">
import { Client, ClientStatusOptions, Industries } from "../../types";
import { useClients } from "../../composables/useClients";
import { initializeClient } from "../../utils/initialize";
import { watchImmediate } from "@vueuse/core";

// Import the createClient function from the composable
const { createClient, updateClient } = useClients();

// Define props with default value
const props = defineProps({
  client: {
    type: Object as PropType<Client>,
    default: initializeClient(),
  },
});

// Use a reactive reference for client state management
const client = ref<Client>(props.client);

// Define refs
const clientStatusOptions = ref(ClientStatusOptions);
const industryOptions = ref(Object.values(Industries));

// Define emits
const emits = defineEmits(["save"]);

// Define computed properties
const editMode = computed(() => !!props.client?.id);

// Watch for changes in the prop and reset if unassigned
watchImmediate(props, (updated) => {
  console.log(`Props Updated: ${updated}`);
  if (!updated.client) {
    client.value = initializeClient();
  } else {
    client.value = updated.client;
  }
});

// Copy billing address to mailing address
const copyBillingAddress = () => {
  client.value.address_line1 = client.value.billing_address_line1;
  client.value.address_line2 = client.value.billing_address_line2;
  client.value.address_city = client.value.billing_address_city;
  client.value.address_state = client.value.billing_address_state;
  client.value.address_postal_code = client.value.billing_address_postal_code;
  client.value.address_country = client.value.billing_address_country;
};

const saveClient = async () => {
  if (editMode.value) {
    // Update Client
    await updateClient(client.value);
  } else {
    // Create Client
    await createClient(client.value);
  }
  emits("save");
};
</script>
