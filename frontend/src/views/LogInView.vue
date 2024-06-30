<template>
  <div class="main">
    <h1 class="main-title">Log <span class="highlight">In</span></h1>
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
      <InputText type="password" placeholder="Password" v-model="password" />
    </InputGroup>
     <!--Send Button-->
     <LogSignButton @click="sendData()" :logIn=true link="http://127.0.0.1:8000/api/v1/login" :values="sendData()" class="button"/>
  </div>
  <Footer />
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import LogSignButton from "@/components/LogSignButton.vue";
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';
  import loginSignUpRequest from "@/types/login";
  import Footer from '@/components/Footer.vue';

  export default defineComponent({
    name: "LogInView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText,
      LogSignButton,
      Footer
    },
    data: function(){
      return {
        email: "",
        password: ""
      }
    },
    methods: {
      sendData() {//Send login credentials to server through button
        if(this.password.length > 8 && this.email.length > 5) {
          const dataArray = ({
            email: this.email,
            password: this.password
          });
          return dataArray;
        }
      }
    }
  });
</script>

<style scoped>
  .main {
    text-align: center;
    margin: 10% 27%;
  }
  .title {
    margin-bottom: 5%;
  }

  .button {
    margin-top: 5%;  
  }
</style>