<template>
  <div
    class="flex flex-column justify-content-center p-3 gap-3"
    :style="{ width: '15rem', height: '100dvh' }"
  >
    <span class="text-sm text-color-secondary uppercase mb-3">Menu</span>
    <router-link to="/dashboard" class="nav-link">
      <Button icon="pi pi-home" rounded outlined />
    </router-link>
    <router-link to="/invoices" class="nav-link">
      <Button icon="pi pi-receipt" rounded outlined />
    </router-link>
    <router-link to="/profile" class="nav-link">
      <Button icon="pi pi-user" rounded outlined />
    </router-link>
    <router-link to="/settings" class="nav-link">
      <Button icon="pi pi-cog" rounded outlined />
    </router-link>
    <div class="flex-grow-1"></div>
    <Button label="Logout" icon="pi pi-sign-out" severity="secondary" />
  </div>
</template>

<style lang="css" scoped>
.nav-link {
  color: var(--primary-color);
  text-decoration: none;
  align-self: center;
  height: 2.25rem;
  display: flex;
  column-gap: 1rem;
  font-size: 1.1rem;
}

.nav-link:hover {
  color: white;
  text-decoration: none;
}

.nav-link i {
  font-size: 1.25rem;
}
</style>
