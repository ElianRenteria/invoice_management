<template>
  <div class="container flex flex-row justify-content-between align-items-center w-full h-auto pb-3 px-6 m-0">
    <InputGroup class="w-8 pt-4">
      <span class="p-input-icon-left w-full rounded-input">
        <i class="pi pi-search" style="color: #637182;"></i>
        <InputText v-model="value" type="text" size="large" placeholder=" search" class="rounded-input-text text-white" />
      </span>
    </InputGroup>
    <div class="w-full h-full flex flex-row justify-content-end align-items-end">
        <i class=" pi pi-star hover:text-pink-700" style="font-size: 2rem; color: #a9a5b5;"></i>
        <i class=" pi pi-bell px-3 hover:text-pink-700" style="font-size: 2rem; color: #a9a5b5;"></i>
        <div class="user-icon ml-6 mt-1 p-2 flex flex-row justify-content-center align-items-center">
          <i class=" pi pi-user" style="font-size: 2rem; color: #a9a5b5;"></i>
        </div>
        <t class="account-name text-2xl px-2">Jack Smith <i class="pi pi-angle-down" style="font-size: 1.2rem; color: #a9a5b5;"></i></t>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import InputText from 'primevue/inputtext';
import InputGroup from 'primevue/inputgroup';
import 'primeicons/primeicons.css'; // Import PrimeIcons CSS

const value = ref('');
</script>

<style scoped>
.user-icon {
  background-color: aliceblue;
  border-radius: 10%;
}
.container {
  margin: 1rem;
  padding: 10px;
  background-color: #140a2c;
  color: #a9a5b5;
}

.p-input-icon-left {
  position: relative;
}

.p-input-icon-left .pi-search {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: #a9a5b5;
}

.p-input-icon-left .p-inputtext {
  padding-left: 2rem;
  width: 100%;
  background-color: #281a4f;
  border: none;
  border-radius: 25px; /* Add border-radius for rounded corners */
}

.rounded-input {
  display: flex;
  align-items: center;
  background-color: #281a4f;
  border-radius: 25px; /* Add border-radius for rounded corners */
  overflow: hidden; /* Ensure children don't overflow the rounded corners */
}

.rounded-input-text {
  flex: 1;
  border: none;
  background-color: transparent;
  padding-left: 2.5rem; /* Adjust padding to account for icon */
  border-radius: 25px; /* Add border-radius for rounded corners */
}

i {
  color: #a9a5b5;
}
</style>
