<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="contact-info">
        <h4>Contact Information</h4>
        <p>Phone: (666) 666-6666</p>
        <p>Email: contact@tsunamisurfers.com</p>
      </div>
      <div class="quick-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About Us</a></li>
          <li><a href="/login">Access account</a></li>
          <li><a href="/signup">Create an account</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024 Tsunami Surfers. All rights reserved.</p>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Footer",
});
</script>

<style scoped>
.footer {
  background-color: #1976d2;
  color: #fff;
  padding: 20px 0;
  text-align: center;
  width: 100%;
}
.footer-container {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}
.footer-container div {
  margin: 10px;
}
.footer-container h4 {
  margin-bottom: 10px;
}
.footer-container ul {
  list-style: none;
  padding: 0;
}
.footer-container ul li {
  margin-bottom: 5px;
}
.footer-container ul li a {
  color: #fff;
  text-decoration: none;
}
.footer-container ul li a:hover {
  text-decoration: underline;
}
.footer-bottom {
  margin-top: 20px;
}
</style>