<template>
  <div class="flex justify-content-center align-content-center w-full h-full">
    <div class="surface-card p-4 shadow-2 border-round">
      <div class="text-center mb-5">
        <div class="text-900 text-3xl font-medium mb-3">Welcome Back!</div>
        <span class="text-600 font-medium line-height-3"
          >Don't have an account?</span
        >
        <a class="font-medium no-underline ml-2 text-blue-500 cursor-pointer"
          >Create today!</a
        >
      </div>

      <div class="text-left">
        <label for="email" class="block text-900 font-medium mb-2">Email</label>
        <InputText
          v-model="form.email"
          id="email"
          type="email"
          class="w-full mb-3"
        />

        <label for="password" class="text-900 font-medium mb-2">Password</label>
        <InputText
          v-model="form.password"
          id="password"
          type="password"
          class="w-full mb-3"
        />

        <div class="flex align-items-center justify-content-between mb-6">
          <div class="flex align-items-center">
            <Checkbox
              id="rememberme"
              :binary="true"
              class="mr-2"
              :disabled="true"
            ></Checkbox>
            <label for="rememberme">Remember me</label>
          </div>
          <a
            class="font-medium no-underline ml-2 text-blue-500 text-right cursor-pointer"
            >Forgot password?</a
          >
        </div>

        <Button
          label="Sign In"
          icon="pi pi-user"
          class="w-full"
          @click="login"
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
  email: undefined,
  password: undefined,
});
const service = new AuthService();
const { setToken, isTokenExpired } = useToken();

const login = async () => {
  if (!form.email || !form.password) {
    console.error("Email and password are required");
    return;
  }
  try {
    const response = await service.login(form.email, form.password);
    if (response.status !== 200) {
      console.error(response.data.message);
      return;
    }
    setToken(response.data.access_token);
    router.push({ name: "Dashboard" });
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
