<template>
  <div
    class="flex flex-row justify-content-start align-items-center gap-0"
    :style="{ width: '100dvw', height: '100vh' }"
  >
    <router-view name="sidebar" />
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<style lang="css">
.container {
  border-radius: 25px;
  height: 100dvh;
  width: 100%;
  background-color: white;
}
</style>
