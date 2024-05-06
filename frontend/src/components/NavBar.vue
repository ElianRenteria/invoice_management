<template>
  <nav class="menu-bar">
    <router-link to="/" class="menu-item">Home</router-link>
    <router-link to="/about" class="menu-item">About</router-link>
  </nav>
</template>

<script>
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
