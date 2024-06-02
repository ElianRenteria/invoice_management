<template>
    <div>
      <nav>
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/clients">Clients</router-link>
        <router-link to="/invoices">Invoices</router-link>
        <router-link to="/services">Services</router-link>
        <router-link to="/settings">Settings</router-link>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: "SidePanelNav",
  };
  </script>
  
  