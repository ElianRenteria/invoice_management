<template>
  <div class="main">
    <h1 class="main-title">Log <span class="highlight">In</span></h1>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText placeholder="Email" v-model="username"/>
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
     <LogSignButton @click="sendData()" :logIn=true link="http://127.0.0.1:8080/api/v1/auth/login" :values="sendData()" class="button"/>
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
        "username": "",
        "password": ""
      }
    },
    methods: {
      sendData() {//Send login credentials to server through button
        if(this.password.length > 8 && this.username.length > 5) {
          const dataArray = ({
            "username": this.username,
            "password": this.password
          });
          return dataArray;
        }
      }
    }
  });
</script>

<style scoped>
  .title {
    margin-bottom: 5%;
  }

  .button {
    margin-top: 5%;  
  }

  .main {
    margin: 3%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 8% 27%;
  }

  .main-title {
    font-size: 4em;
    text-align: center;
  }

  .highlight {
    color: rgb(0,212,255);
    color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
  }
</style>