<template>
  <div
    class="sidebar flex flex-column justify-content-center p-5 gap-3"
    :style="{ width: '10rem' }"
  >
    <span class="text-sm text-color-secondary uppercase mb-3">Menu</span>
    <router-link to="/" :class="['nav-link', { active: isActive('Home') }]">
      <i class="pi pi-home"></i>
      <span>Home</span>
    </router-link>
    <router-link
      to="/invoices"
      :class="['nav-link', { active: isActive('Invoices') }]"
    >
      <i class="pi pi-receipt"></i>
      <span>Invoices</span>
    </router-link>
    <router-link
      to="/clients"
      :class="['nav-link', { active: isActive('Clients') }]"
    >
      <i class="pi pi-users"></i>
      <span>Clients</span>
    </router-link>
    <router-link
      to="/profile"
      :class="['nav-link', { active: isActive('Profile') }]"
    >
      <i class="pi pi-user"></i>
      <span>Profile</span>
    </router-link>
    <div class="flex-grow-1"></div>
    <router-link
      to="/settings"
      :class="['nav-link', { active: isActive('Settings') }]"
    >
      <i class="pi pi-cog"></i>
      <span>Settings</span>
    </router-link>
    <router-link to="/logout" class="nav-link">
      <i class="pi pi-sign-out"></i>
      <span>Logout</span>
    </router-link>
  </div>
</template>

<style lang="css" scoped>
.sidebar:hover {
  /* TODO: Implement Some Sort of Expandable Sidebar and Toggle Span Display */
}

.nav-link {
  color: var(--text-color-secondary);
  text-decoration: none;
  align-self: center;
  display: flex;
  flex-direction: row;
  column-gap: 0.5rem;
  width: 4rem;
  height: 4rem;
  padding: 1.25rem;
  border-radius: 2rem;
  transition: background-color 0.35s;
}
.nav-link.active {
  color: var(--primary-color-reverse);
  background-color: var(--surface-100);
}
.nav-link:hover {
  background-color: var(--surface-100);
  color: var(--primary-color);
}

.nav-link span {
  display: none;
}
/* .nav-link:hover span {
  display: inline;
} */

.nav-link i {
  font-size: 1.5rem;
}
</style>

<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute();
const isActive = (routeName: string) => route.name?.toString() === routeName;
</script>
