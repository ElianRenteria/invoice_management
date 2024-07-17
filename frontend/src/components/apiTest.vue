<template>
  <Button label="Click" @click="makeAPICall" />
</template>

<script lang="ts">
import { ref } from "vue";
import Button from "primevue/button";

export default {
  components: {
    Button,
  },
  setup() {
    const makeAPICall = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000");
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error("Error making API call:", error);
      }
    };

    return {
      makeAPICall,
    };
  },
};
</script>


