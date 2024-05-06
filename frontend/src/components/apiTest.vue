<template>
  <Button label="Click" @click="makeAPICall" />
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
    msg: String,
  },
  methods: {
    async makeAPICall() {
      try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error making API call:', error);
      }
    }
  }
});
</script>
