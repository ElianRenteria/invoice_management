<template>
  <div class="flex justify-content-center align-content-center w-full h-full">
    <div class="surface-card p-4 shadow-2 border-round">
      <div class="text-center mb-5">
        <div class="text-900 text-3xl font-medium mb-3">New Here?</div>
        <span class="text-600 font-medium line-height-3">
          Already have an account?
        </span>
        <RouterLink
          to="/login"
          class="font-medium no-underline ml-2 text-blue-500 cursor-pointer"
        >
          Log in here!
        </RouterLink>
      </div>

      <div class="text-left">
        <label for="firstname" class="block text-900 font-medium mb-2">
          First Name
        </label>
        <InputText
          v-model="form.firstname"
          id="firstname"
          type="text"
          placeholder="Johnny"
          class="w-full mb-3"
        />

        <label for="lastname" class="block text-900 font-medium mb-2">
          Last Name
        </label>
        <InputText
          v-model="form.lastname"
          id="lastname"
          type="text"
          placeholder="Appleseed"
          class="w-full mb-3"
        />

        <label for="email" class="block text-900 font-medium mb-2">Email</label>
        <InputText
          v-model="form.email"
          id="email"
          type="email"
          placeholder="johnnyappleseed@example.com"
          class="w-full mb-3"
        />

        <label for="password" class="text-900 font-medium mb-2">Password</label>
        <InputText
          v-model="form.password"
          id="password"
          type="password"
          class="w-full mb-3"
        />

        <Button
          label="Create Account"
          icon="pi pi-user-plus"
          class="w-full"
          @click="signup"
        ></Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AuthService from "../../../services/auth/AuthService";
import { useToken } from "../../../composables/useToken";
import { useRouter } from "vue-router";

const router = useRouter();
const form = reactive({
  firstname: undefined,
  lastname: undefined,
  email: undefined,
  password: undefined,
});
const service = new AuthService();
const { isTokenExpired } = useToken();

const signup = async () => {
  if (!form.email || !form.password || !form.firstname || !form.lastname) {
    console.error("All fields are required");
    return;
  }
  try {
    const response = await service.register(
      form.email,
      form.password,
      form.firstname,
      form.lastname,
    );
    if (response.status == 400) {
      const message = response.data.detail;
      console.error("Registration Error: ", message);
    } else if (response.status == 200) {
      console.log("Registration Successful");
      router.push({ name: "Login" });
    } else {
      console.error("An Unknown Error Occurred");
    }
  } catch (error) {
    console.error(error);
  }
};

onBeforeMount(() => {
  if (!isTokenExpired()) {
    router.push({ name: "Dashboard" });
  }
});
</script>
