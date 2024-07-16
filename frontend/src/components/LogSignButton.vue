<template>
  <div>
    <Button :label="logIn ? 'Log In' : 'Sign Up'" @click="sendData(link)" rounded/>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Button from "primevue/button";

export default defineComponent({
  name: "LogSignButton",
  components: {
    Button,
  },
  props: {
    logIn: Boolean,
    link: String,
    values: Array,
  },
  setup(props) {
    const sendData = async (link: string) => {
      try {
        const response = await fetch(link, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(props.values),
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
      sendData,
    };
  },
});
</script>

