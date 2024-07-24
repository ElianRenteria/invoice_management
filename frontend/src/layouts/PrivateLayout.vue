<template>
  <div class="container">
    <div class="flex justify-content-between px-5" :style="{ width: '100dvw' }">
      <h1>Invoice Management</h1>
      <div class="flex flex-row align-items-center gap-3">
        <Button :size="'large'" icon="pi pi-bell" rounded />
        <Avatar
          label="SB"
          :size="'large'"
          :shape="'circle'"
          :class="['surface-section', 'text-color-secondary']"
        />
      </div>
    </div>
    <div
      class="flex justify-content-start align-items-stretch gap-0"
      style="height: calc(100vh - 6rem)"
    >
      <router-view name="sidebar" />
      <router-view
        class="w-full surface-ground border-round-3xl border-noround-right p-3"
      />
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
  height: 100dvh;
}
/* .container {
  background-color: white;
  border-radius: 4em 0 0 4em;
} */
</style>
