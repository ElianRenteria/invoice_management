<template>
    <nav class="menu-bar">
      <h1>Invoice Manager</h1>
      <div class="items">
        <router-link to="/" class="menu-item">Home</router-link>
        <router-link to="/about" class="menu-item">About</router-link>
        <router-link to="/login" class="menu-item">Log In</router-link>
        <router-link to="/signup" class="menu-item">Sign Up</router-link>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
  </script>
  
  <style scoped>
  .menu-bar {
    background-color: #1976d2; /* Set background color */
    color: #ffffff; /* Set text color */
    padding: 10px; /* Add padding */
    padding-left: 30px; /* Add padding to the left */
    padding-right: 30px; /* Add padding to the right */
    width: 100%; /* Set full width */
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .menu-bar .items {
    min-width: 300px;
    width: 25%;
    height: 100%;
    paddin: 0%;
    margin: 0%;
    padding-right: 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  
  .menu-item {
    text-decoration: none; /* Remove underline from links */
    color: #ffffff; /* Set text color */
    margin-right: 10px; /* Add margin between menu items */
  }
  
  .menu-item:hover {
    color: #072038;
  }
  </style>