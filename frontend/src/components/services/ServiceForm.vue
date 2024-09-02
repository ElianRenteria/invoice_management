<template>
    <div class="flex flex-row gap-3 my-3">
      <div class="flex flex-column gap-2">
        <label for="name">Name</label>
        <InputText id="name" v-model="service.name" />
        <label for="name" class="text-xs text-color-secondary">
          name of service
        </label>
      </div>
      
      <div class="flex flex-column gap-2">
        <label for="price">Price</label>
        <InputNumber id="price" v-model="service.price" />
        <label for="name" class="text-xs text-color-secondary">
          Price of Service per unit
        </label>
      </div>
    </div>
    <div class="p-fluid mt-3">
      <Button
        :label="editMode ? 'Update' : 'Save'"
        :icon="editMode ? 'pi pi-pencil' : 'pi pi-save'"
        class="flex-grow"
        @click="saveService"
      />
    </div>
  </template>
  
  <script setup lang="ts">
  import { Service } from "../../types/Service";
  import { useServices } from "../../composables/useServices";
  import { initializeService } from "../../utils/initialize";
  import { watchImmediate } from "@vueuse/core";
  
  // Import the createService function from the composable
  const { createService } = useServices();
  
  // Define props with default value
  const props = defineProps({
    service: {
      type: Object as PropType<Service>,
      default: initializeService(),
    },
  });
  
  // Use a reactive reference for service state management
  const service = ref<Service>(props.service);
  
  // Define emits
  const emits = defineEmits(["save"]);
  
  // Define computed properties
  const editMode = computed(() => !!props.service?.id);
  
  // Watch for changes in the prop and reset if unassigned
  watchImmediate(props, (updated) => {
    if (!updated.service) {
      service.value = initializeService();
    } else {
      service.value = updated.service;
    }
  });
  
  const saveService = async () => {
    if (editMode.value) {
      // Update Service
      // await updateService(props.service);
    } else {
      // Create Service
      await createService(props.service);
    }
    emits("save");
  };
  </script>