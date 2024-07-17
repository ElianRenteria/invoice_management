<template>
  <div class="main">
    <h1 class="main-title">Log <span class="highlight">In</span></h1>
    <!-- Username -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText placeholder="Email" v-model="email" />
    </InputGroup>
    <br />
    <!-- Password -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText type="password" placeholder="Password" v-model="password" />
    </InputGroup>
    <!-- Send Button -->
    <LogSignButton @click="sendData" :logIn="true" :link="loginEndpoint" :values="sendData" class="button" />
  </div>
  <Footer />
</template>

<script setup lang="ts">
import { ref } from "vue";
import LogSignButton from "@/components/LogSignButton.vue";
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import Footer from '@/components/Footer.vue';
    // Reactive variables
    const email = ref("");
    const password = ref("");

    // Computed property or constant for login endpoint
    const loginEndpoint = "http://0.0.0.0:8080/api/v1/login";

    // Method to send login data
    const sendData = () => {
      if (password.value.length > 8 && email.value.length > 5) {
        const dataArray = {
          email: email.value,
          password: password.value,
        };
        return dataArray;
      }
    };
</script>

<style scoped>
.main {
  text-align: center;
  margin: 10% 27%;
}

.main-title {
  margin-bottom: 5%;
}

.button {
  margin-top: 5%;
}
</style>
