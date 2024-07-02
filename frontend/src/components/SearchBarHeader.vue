<template>
    <div class="container">
        <InputText v-model="value1" type="text" size="large" placeholder="search" style="background-color: #281a4f; border: none;"/>
    </div>"
</template>
  
<script lang="ts">
  import { defineComponent } from "vue";
  import InputText from 'primevue/inputtext';
  
  export default defineComponent({
    name: "SearchBarHeader",
    components: {
      InputText,
    },
  });
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    margin: 1rem;
    padding: 10px;
    background-color: #140a2c;
    color: #a9a5b5;
  }
</style>