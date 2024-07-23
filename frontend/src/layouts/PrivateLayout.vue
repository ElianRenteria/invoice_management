<template>
  <div
    class="flex justify-content-between align-items-center p-5"
    :style="{ width: '100dvw' }"
  >
    <h1>Invoice Management</h1>
    <div class="flex flex-row align-items-center gap-3">
      <Button icon="pi pi-bell" rounded />
      <Avatar label="SB" :size="'large'" />
    </div>
  </div>
  <div class="flex flex-row justify-content-start gap-0">
    <router-view name="sidebar" />
    <div class="container w-full">
      <router-view />
    </div>
  </div>
  <!-- <div
    class="flex flex-row justify-content-start align-items-center gap-0"
    :style="{ width: '100dvw', height: '100vh' }"
  >
    <router-view name="sidebar" />
    <div class="container">
      <router-view />
    </div>
  </div> -->
</template>

<style lang="css">
.container {
  border-radius: 25px;
  background-color: white;
  align-items: stretch;
}
</style>
