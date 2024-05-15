<template>
  <div class="main">
    <h1 class="title">Log In</h1>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText placeholder="Email" v-model="email"/>
    </InputGroup>
    <br>
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText placeholder="Password" v-model="password"/>
    </InputGroup>
     <!--Send Button-->
     <LogSignButton :logIn=true link="http://127.0.0.1:8000/login/" class="button"/>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import LogSignButton from "@/components/LogSignButton.vue"; 
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';

  export default defineComponent({
    name: "LogInView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText,
      LogSignButton
    },
    data: function(){
      return {
        email: "",
        password: "",
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