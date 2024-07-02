<template>
    <div class="container">
      <nav>
        <p>Invoice Manager</p>
        <router-link to="/dashboard"><i class="pi pi-th-large" style="font-size: 1.2rem"></i>Dashboard</router-link>
        <router-link to="/clients"><i class="pi pi-users" style="font-size: 1.2rem"></i>Clients</router-link>
        <router-link to="/invoices"><i class="pi pi-file" style="font-size: 1.2rem"></i>Invoices</router-link>
        <router-link to="/services"><i class="pi pi-wrench" style="font-size: 1.2rem"></i>Services</router-link>
        <router-link to="/settings"><i class="pi pi-cog" style="font-size: 1.2rem"></i>Settings</router-link>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: "SidePanelNav",
  };
  </script>

<style scoped>
  i{
    margin-right: 10px;
  }
  p{
    color: #ffffff;
    font-size: 1.1rem;
    width: 100%;
    margin: 0;
  }
  .container{
    min-width: 200px;
    max-width: 15%;
    height: 100%;
    padding: 0px;
    margin: 0%;
    background-color: #211641;
    color: #a5a2b6;
  }
  .container, nav, router-link{
    padding-left: 30%;
  }
  .container nav {
    background-color: #211641; /* Set background color */
    color: #a5a2b6; /* Set text color */
    width: 100%; /* Set full width */    height: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: start;
  }
  router-link{
    font-size: 1.5 rem;
  }
  nav a {
    text-decoration: none; /* Remove underline from links */
    color: #a5a2b6; /* Set text color */
    margin-right: 10px; /* Add margin between menu items */
  }
  
  nav a:hover {
    color: #d058f1;
  }
</style>
  
  