<template>
  <div class="flex flex-column gap-5 w-4">
    <div class="flex flex-column gap-2">
      <label for="invoice-name">Name</label>
      <InputText id="invoice-name" v-model="name" aria-describedby="username-help" />
      <small id="invoice-help">Enter invoice name</small>
    </div>

    <div class="flex flex-column gap-2">
      <label for="invoice-date">Date</label>
      <Calendar id="invoice-date" v-model="date" dateFormat="dd/mm/yy"/>
    </div>
    
    <div id="label" class="flex flex-row gap-4">

    </div>

  </div>
  
  
</template>

<style lang="css" scoped>

</style>
  
<script setup lang="ts">
  const name = undefined;
  const date = undefined;
</script>