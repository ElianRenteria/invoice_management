<template>
  <div class="main">
    <h1 class="title">Sign Up</h1>
    <!--Name-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-id-card"></i>
      </InputGroupAddon>
      <InputText placeholder="Full Name" v-model="name"/>
    </InputGroup>
    <br>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-user"></i>
      </InputGroupAddon>
      <InputText placeholder="Username" v-model="username"/>
    </InputGroup>
    <br>
    <!--Email-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText type="text" placeholder="Email" v-model="email" id="email"/>
    </InputGroup>
    <br>
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <InputText placeholder="Password" v-model="password" id="pass"/>
    </InputGroup>
     <!--Send Button-->
     <LogSignButton @click="sendData()" :logIn=false link="http://127.0.0.1:8000/signup" :values="sendData()" class="button"/>
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
    data: function(){
      return{
        name: "",
        username: "",
        email: "",
        password: "",
        dataArray: [] as string [],
      }
    },
    methods: {
      sendData() {//Send sign up credentials to server through button
        this.dataArray = [this.name, this.username, this.email, this.password];
        return this.dataArray;
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
  