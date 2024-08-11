<template>
  <div class="flex justify-content-start align-content-center w-full h-full">
    <div class="surface-card p-4 shadow-2 border-round">
      <div class="text-center mb-5">
        <div class="text-900 text-3xl font-medium mb-3">Welcome Back!</div>
        <span class="text-600 font-medium line-height-3"
          >Don't have an account?</span
        >
        <RouterLink
          to="/register"
          class="font-medium no-underline ml-2 text-blue-500 cursor-pointer"
        >
          Create today!
        </RouterLink>
      </div>

      <InlineMessage severity="error" class="block mb-3" v-if="errorMessage">
        {{ errorMessage }}
      </InlineMessage>

      <div>
        <label for="email" class="block text-left text-900 font-medium mb-2">
          Email
        </label>
        <InputText
          v-model="form.email"
          id="email"
          type="email"
          class="w-full mb-3"
          @change="validateEmail"
          :invalid="validity.email === false"
        />

        <label for="password" class="block text-left text-900 font-medium mb-2">
          Password
        </label>
        <InputText
          v-model="form.password"
          id="password"
          type="password"
          class="w-full mb-3"
          @change="validatePassword"
          :invalid="validity.password === false"
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
          :disabled="!(validity.email && validity.password)"
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
const form = reactive<{
  email: string | undefined;
  password: string | undefined;
}>({
  email: undefined,
  password: undefined,
});
const validity = reactive<{
  email: boolean | undefined;
  password: boolean | undefined;
}>({
  email: undefined,
  password: undefined,
});
const errorMessage = ref<string | undefined>(undefined);
const service = new AuthService();
const { setToken, isTokenExpired } = useToken();

const validateEmail = () => {
  const pattern = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  validity.email = pattern.test(form.email ?? "");
};

const validatePassword = () => {
  validity.password = form.password !== undefined && form.password.length > 0;
};

const login = async () => {
  if (!form.email || !form.password) {
    console.error("Email and password are required");
    errorMessage.value = "Email and password are required";
    return;
  }
  try {
    const response = await service.login(form.email, form.password);
    if (response.status !== 200) {
      console.error(response.data.detail);
      errorMessage.value = response.data.detail;
      return;
    }
    setToken(response.data.access_token);
    router.push({ name: "Dashboard" });
  } catch (error) {
    errorMessage.value = "Unexpected error occurred";
    console.error(error);
  }
};

onBeforeMount(() => {
  if (!isTokenExpired()) {
    router.push({ name: "Dashboard" });
  }
});
</script>
