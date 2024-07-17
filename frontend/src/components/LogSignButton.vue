<template>
  <div>
    <Button :label="logIn.value ? 'Log In' : 'Sign Up'" @click="sendData()" rounded />
  </div>
</template>

<script lang="ts">
import { ref } from "vue";
import Button from "primevue/button";

export default {
  name: "LogSignButton",
  components: {
    Button,
  },
  setup() {
    const logIn = ref(false);
    const link = ref("http://0.0.0.0:8080/api/v1/login");
    const values = ref([]);

    const sendData = async () => {
      try {
        const response = await fetch(link.value, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values.value),
        });

        if (response.ok) {
          const data = await response.json();
          console.log(data);
          console.log("Sent Data");
          // Example: redirect user on successful login/signup
          // router.push({ name: 'dashboard' });
        } else {
          alert("User already exists");
        }
      } catch (error) {
        console.error("Error making API call:", error);
      }
    };

    return {
      logIn,
      link,
      values,
      sendData,
    };
  },
};
</script>


