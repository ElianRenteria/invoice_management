<template>
  <div class="container h-full w-2">
    <nav class="flex flex-column justify-content justify-content-start align-items-start h-auto mx-2 md:text-md lg:text-lg xl:text-xl">
      <t class="md:text-lg lg:text-xl xl:text-2xl mt-3 text-white-alpha-80 font-medium p-4">Invoice Manager</t>
      <router-link to="/dashboard" class="ml-2 mt-6 p-3"><i class="pi pi-th-large" style="font-size: 1.25rem"></i>Dashboard</router-link>
      <router-link to="/clients" class="ml-2 mt-2 p-3"><i class="pi pi-users" style="font-size: 1.25rem"></i>Clients</router-link>
      <router-link to="/invoices" class="ml-2 mt-2 p-3"><i class="pi pi-file" style="font-size: 1.25rem"></i>Invoices</router-link>
      <router-link to="/services" class="mb-8 ml-2 mt-2 p-3"><i class="pi pi-wrench" style="font-size: 1.25rem"></i>Services</router-link>
      <hr class="mt-8 pl-8 pr-8 w-10 h-full white-line">
      <router-link to="/settings" class="mb-8 ml-2 mt-3 p-3"><i class="pi pi-cog" style="font-size: 1.25rem"></i>Settings</router-link>
    </nav>
  </div>
</template>

<script>
  export default {
    name: "SidePanelNav",
  };
</script>

<style scoped>
.container {
  background-color: #211641;
  color: #a9a5b5;
}
.white-line {
  border: none;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
i {
  margin-right: 0.25rem;
}
p {
  color: #ffffff;
  font-size: 1.1rem;
  width: 100%;
  margin: 0;
}
router-link {
  font-size: 1.5rem;
}
nav a {
  text-decoration: none; /* Remove underline from links */
  color: #a5a2b6; /* Set text color */
  margin-right: 0.25rem; /* Add margin between menu items */
}
nav a:hover,
nav .router-link-active,
nav .router-link-exact-active {
  color: #d058f1;
}
</style>

  
  