<template>
  <div class="main">
    <h1 class="title">Log In</h1>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText placeholder="Email" />
    </InputGroup>
    <br>
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText placeholder="Password" />
    </InputGroup>
     <!--Send Button-->
     <apiTest msg="Log In" class="button"/>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';

  export default defineComponent({
    name: "LogInView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText
    },
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