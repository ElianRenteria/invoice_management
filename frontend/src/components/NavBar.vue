<template>
  <nav class="menu-bar">
    <h1>Invoice Manager</h1>
    <router-link to="/" class="menu-item">Home</router-link>
    <router-link to="/about" class="menu-item">About</router-link>
    <router-link to="/login" class="menu-item">Log In</router-link>
    <router-link to="/signup" class="menu-item">Sign Up</router-link>
  </nav>
</template>

<script>
import Menubar from 'primevue/menubar';
export default {
  name: "NavBar",
};
</script>

<style scoped>
.menu-bar {
  background-color: #1976d2; /* Set background color */
  color: #ffffff; /* Set text color */
  padding: 10px; /* Add padding */
}

.menu-item {
  text-decoration: none; /* Remove underline from links */
  color: #ffffff; /* Set text color */
  margin-right: 10px; /* Add margin between menu items */
}

.menu-item:hover {
  text-decoration: underline; /* Add underline on hover */
}
</style>
