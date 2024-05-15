<template>
  <div class="main">
    <h1 class="title">Sign Up</h1>
    <!--Name-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-id-card"></i>
      </InputGroupAddon>
      <InputText placeholder="Full Name" />
    </InputGroup>
    <br>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-user"></i>
      </InputGroupAddon>
      <InputText placeholder="Username" />
    </InputGroup>
    <br>
    <!--Email-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText type="text" placeholder="Email" id="confirmPass"/>
    </InputGroup>
    <br>
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText placeholder="Password" id="pass"/>
    </InputGroup>
     <!--Send Button-->
     <LogSignButton :logIn=false link="http://127.0.0.1:8000/signup" class="button"/>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';
  import LogSignButton from "@/components/LogSignButton.vue";

  export default defineComponent({
    name: "SignUpView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText,
      LogSignButton
    },
    methods: {
      matchPasswords() {
        const pass = document.getElementById("pass");
      }
    }
  });
</script>

<style>
  .main {
    text-align: center;
    margin: 8% 27%;
  }
  .title {
    margin-bottom: 5%;
  }

  .button {
    margin-top: 5%;  
  }
</style>
  