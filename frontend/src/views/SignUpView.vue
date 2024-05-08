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
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText placeholder="Password" id="pass"/>
    </InputGroup>
    <br>
    <!--Confirm Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-sync"></i>
      </InputGroupAddon>
      <InputText type="text" placeholder="Confirm Password" id="confirmPass"/>
    </InputGroup>
     <!--Send Button-->
     <apiTest msg="Sign Up" class="button"/>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';

  export default defineComponent({
    name: "SignUpView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText
    },
    methods: {
      matchPasswords() {
        const pass = document.getElementById("pass");
        const confirmPass = document.getElementById("confirmPass");
        
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
  