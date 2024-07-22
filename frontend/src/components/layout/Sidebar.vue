<template>
  <div
    class="flex flex-column justify-content-start surface-800 p-3 gap-2"
    :style="{ width: '15rem', height: '100dvh' }"
  >
    <h1 class="text-white mb-5">Invoice Management</h1>
    <nav class="align-items-start">
      <router-link to="/dashboard" class="nav-link">
        <i class="pi pi-home"></i>
        Dashboard
      </router-link>
      <router-link to="/profile" class="nav-link">
        <i class="pi pi-user"></i>
        Profile
      </router-link>
      <router-link to="/settings" class="nav-link">
        <i class="pi pi-cog"></i>
        Settings
      </router-link>
    </nav>
    <div class="flex-grow-1"></div>
    <Button label="Logout" icon="pi pi-sign-out" severity="secondary" />
  </div>
</template>

<style lang="css" scoped>
.nav-link {
  color: var(--primary-color);
  text-decoration: none;
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
