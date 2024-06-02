<template>
  <div class="home">
    <Image src="@/assets/placeholder.png" alt="Image" width="650" />
    <h1>Main title</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Knob from 'primevue/knob';
import Image from 'primevue/image';

export default defineComponent({
  name: "HomeView",
  components: {
    Image,
    Knob
  },
});
</script>
