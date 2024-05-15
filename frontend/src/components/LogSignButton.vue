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
  name: "apiTest",
  components: {
    Button,
  },
  props: {
    logIn: Boolean,
    link: String
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
        xhr.open("POST", "http://127.0.0.1:8000/login", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            value: "value"
        }));
        console.log("sent");
      } catch(error) {
        console.error('Error making API call:', error);
      }
    }
  },
  data: function(){
      return {
        link: ""
      }
    }
});
</script>
