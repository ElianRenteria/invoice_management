<template>
  <div v-if="logIn">
    <Button label="Log In" @click="sendData(link)" rounded/>
  </div>
  <div v-else>
    <Button label="Sign Up" @click="sendData(link)" rounded/>
  </div>
</template>

<script lang="ts">
import Button from "primevue/button";
import { defineComponent } from "vue";

export default defineComponent({
  name: "LogSignButton",
  components: {
    Button,
  },
  props: {
    logIn: Boolean,
    link: String,
    values: Array  //Array of either sign up or log in creds 
  },
  methods: {
    async makeAPICall(link:string) {
      try {
        const response = await fetch(link);
        const data = await response.json();
        console.log(data);
        console.log("worked");
      } catch (error) {
        console.error('Error making API call:', error);
      }
    },
    async sendData(link:string) {
      try {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", link, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify(this.values));
        console.log("Sent Data");

        xhr.onreadystatechange = async function() {
          //Send user to the dashboard
          if(xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
          } else {
            alert("User already exists")
          }
        }
        
      } catch(error) {
        console.error('Error making API call:', error);
      }
    },
    redirect() {
      //Send user to dashboard after they been verified
      this.$router.push({name: 'home'});
    }
  },
});
</script>
