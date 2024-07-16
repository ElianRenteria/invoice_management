<template>
  <div class="main">
    <h1 class="main-title">Sign <span class="highlight">Up</span></h1>
    <!-- Name -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-id-card"></i>
      </InputGroupAddon>
      <InputText placeholder="Full Name" required :invalid="!validName" v-model="name" @blur="validateName" />
    </InputGroup>
    <br />
    <!-- Username -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-user"></i>
      </InputGroupAddon>
      <InputText placeholder="Username" required :invalid="!validUsername" v-model="username" @blur="validateUsername" />
    </InputGroup>
    <br />
    <!-- Email -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText type="text" placeholder="Email" required :invalid="!validEmail" v-model="email" @blur="validateEmail" id="email" />
    </InputGroup>
    <br />
    <!-- Password -->
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-key"></i>
      </InputGroupAddon>
      <Password placeholder="Password" v-model="password" :weakLabel="'Too simple'" :mediumLabel="'Average complexity'" :strongLabel="'Complex password'" :promptLabel="'Choose a password'" :invalid="!validPassword" @blur="validatePassword" />
    </InputGroup>
    <!-- Send Button -->
    <LogSignButton @click="sendData" :logIn="false" :link="signupEndpoint" :values="sendData" class="button" />
  </div>
  <Footer />
</template>

<script lang="ts">
import { ref } from "vue";
import Footer from '@/components/Footer.vue';
import LogSignButton from "@/components/LogSignButton.vue";
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';

export default {
  name: "SignUpView",
  components: {
    Footer,
    LogSignButton,
    InputGroup,
    InputGroupAddon,
    InputText,
    Password,
  },
  setup() {
    // Reactive variables
    const name = ref("");
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const validName = ref(true);
    const validUsername = ref(true);
    const validEmail = ref(true);
    const validPassword = ref(true);

    // Computed property or constant for signup endpoint
    const signupEndpoint = "http://0.0.0.0:8080/api/v1/signup";

    // Method to validate name
    const validateName = () => {
      if (name.value.length >= 5 && name.value.includes(" ")) {
        validName.value = true;
      } else {
        validName.value = false;
      }
    };

    // Method to validate username
    const validateUsername = () => {
      if (username.value.length >= 4) {
        validUsername.value = true;
      } else {
        validUsername.value = false;
      }
    };

    // Method to validate password
    const validatePassword = () => {
      if (password.value.length > 8) {
        validPassword.value = true;
      } else {
        validPassword.value = false;
      }
    };

    // Method to validate email
    const validateEmail = () => {
      const regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      if (regex.test(email.value)) {
        validEmail.value = true;
      } else {
        validEmail.value = false;
      }
    };

    // Method to send signup data
    const sendData = () => {
      if (validName.value && validUsername.value && validEmail.value && validPassword.value) {
        const dataArray = {
          name: name.value,
          username: username.value,
          email: email.value,
          password: password.value,
        };
        return dataArray;
      } else {
        alert("Form is not complete");
      }
    };

    return {
      name,
      username,
      email,
      password,
      validName,
      validUsername,
      validEmail,
      validPassword,
      sendData,
      signupEndpoint,
      validateName,
      validateUsername,
      validateEmail,
      validatePassword,
    };
  },
};
</script>

<style scoped>
.main {
  text-align: center;
  margin: 8% 27%;
}

.main-title {
  margin-bottom: 5%;
}

.button {
  margin-top: 5%;
}
</style>
