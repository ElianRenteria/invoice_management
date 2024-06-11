<template>
  <div class="main">
    <h1 class="main-title">Sign <span class="highlight">Up</span></h1>
    <!--Name-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-id-card"></i>
      </InputGroupAddon>
      <InputText placeholder="Full Name" required :invalid="validName ? false : true" v-model="name" @blur="validateName"/>
    </InputGroup>
    <br>
    <!--Username-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-user"></i>
      </InputGroupAddon>
      <InputText placeholder="Username" required :invalid="validUsername ? false : true" v-model="username" @blur="validateUsername" />
    </InputGroup>
    <br>
    <!--Email-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-envelope"></i>
      </InputGroupAddon>
      <InputText type="text" placeholder="Email" required :invalid="validEmail ? false : true" v-model="email" @blur="validateEmail" id="email"/>
    </InputGroup>
    <br>
     <!--Password-->
    <InputGroup>
      <InputGroupAddon>
          <i class="pi pi-key"></i>
      </InputGroupAddon>
      <Password placeholder="Password" v-model="password" :invalid="validPassword ? false : true" @blur="validatePassword" promptLabel="Choose a password" weakLabel="Too simple" mediumLabel="Average complexity" strongLabel="Complex password" />
      <!--<InputText placeholder="Password" required :invalid="validPassword ? false : true" v-model="password" @blur="validatePassword" id="pass"/>-->
    </InputGroup>
     <!--Send Button-->
     <LogSignButton @click="sendData()" :logIn=false link="http://127.0.0.1:8000/api/v1/signup" :values="sendData()" class="button"/>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  import apiTest from "@/components/apiTest.vue"; // @ is an alias to /src
  import InputGroup from 'primevue/inputgroup';
  import InputGroupAddon from 'primevue/inputgroupaddon';
  import InputText from 'primevue/inputtext';
  import LogSignButton from "@/components/LogSignButton.vue";
  import Password from 'primevue/password';

  export default defineComponent({
    name: "SignUpView",
    components: {
      apiTest,
      InputGroup,
      InputGroupAddon,
      InputText,
      LogSignButton,
      Password
    },
    data: function(){
      return{
        name: "",
        username: "",
        email: "",
        password: "",
        validEmail: true,
        validName: true, 
        validUsername: true, 
        validPassword: true
      }
    },
    methods: {
      validateName(){
        // Validate that name is long enough and contains space
        if (this.name.length >= 5 && this.name.includes(' ')) {
          this.validName = true;
        } else {
          this.validName = false;
        }
      },
      validateUsername() {
        //Validate username is long enough
        if(this.username.length >= 4) {
          this.validUsername = true;
        } else {
          this.validUsername = false;
        }
      },
      validatePassword() {
        //Validate Password is long enough
        if(this.password.length > 8) {
          this.validPassword = true;
        } else {
          this.validPassword = false;
        }
      },
      validateEmail() {
        // Validate that email contains @ and .
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email)) {
          this.validEmail = true;
        } else {
          this.validEmail = false;
        }
      },
      sendData() {//Send sign up credentials to server through button
        if(this.validName && this.validUsername && this.validEmail && this.validPassword) {
          const dataArray = ({
            name: this.name,
            username: this.username,
            email: this.email,
            password: this.password
          });
          return dataArray;
        } else {
          alert("Form is not complete")
        }
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
  