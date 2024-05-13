<template>
  <div v-if="logIn">
    <Button label="Log In" @click="makeAPICall(link)" rounded/>
  </div>
  <div v-else>
    <Button label="Sign Up" @click="makeAPICall(link)" rounded/>
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
    }
  }
});
</script>
