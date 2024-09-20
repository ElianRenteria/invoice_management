<template>
  <div class="container">
    <div class="flex justify-content-between px-5">
      <div class="flex gap-2 align-items-center">
        <svg
          width="64"
          height="64"
          viewBox="0 0 37 64"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <rect
            x="8"
            y="8"
            width="37"
            height="48"
            rx="4"
            ry="4"
            fill="#f8fafc"
            stroke="#e8defd"
            stroke-width="1"
          />
          <rect x="16" y="14" rx="3" width="22" height="6" fill="#b99dfa" />
          <rect x="16" y="26" rx="1" width="22" height="2" fill="#dccefc" />
          <rect x="16" y="32" rx="1" width="22" height="2" fill="#dccefc" />
          <rect x="16" y="38" rx="1" width="22" height="2" fill="#dccefc" />
          <text x="34" y="51" fill="#a27df8" font-size="9" font-weight="light">
            $
          </text>
        </svg>
        <h1>Merces <span class="font-light">Lite</span></h1>
      </div>
      <div class="flex flex-row align-items-center gap-3">
        <Button :size="'large'" icon="pi pi-bell" rounded />
        <Avatar
          :label="initials"
          :size="'large'"
          :shape="'circle'"
          :class="['surface-section', 'text-color-secondary']"
        />
      </div>
    </div>
    <div
      class="flex justify-content-start align-items-stretch gap-0"
      style="min-height: calc(100vh - 6rem)"
    >
      <router-view name="sidebar" />
      <router-view
        class="w-full surface-ground border-round-3xl border-noround-right p-3"
      />
      <Toast />
    </div>
  </div>
</template>

<style lang="css" scoped>
.container {
  height: 100dvh;
}
.container div:first-child {
  width: 100dvw;
}
</style>

<script setup lang="ts">
import { useCurrentUser } from "../composables/useCurrentUser";
const { user, initials } = useCurrentUser();
</script>
