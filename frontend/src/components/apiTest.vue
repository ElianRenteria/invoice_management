<template>
  <Button label={msg} :class="{msg}" @click="makeAPICall" rounded/>
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
        const response = await fetch('http://127.0.0.1:8000');
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error making API call:', error);
      }
    }
  }
});
</script>
