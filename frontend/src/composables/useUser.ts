// src/composables/useUser.ts
import { ref, onMounted } from "vue";
import apiClient from "@/services/http_client";
import { User } from "@/types/User";

export function useUser() {
  const profile = ref<User | undefined>(undefined);
  const isLoading = ref(false);
  const error = ref<any>(null);

  const fetchUser = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      // TODO: Change the return type to Invoice[] once a type is defined
      const response = await apiClient.get<User>("/auth/me");
      profile.value = response.data;
    } catch (err) {
      error.value = err;
    } finally {
      isLoading.value = false;
    }
  };

  // Automatically fetch invoices when the component using this composable is mounted
  onMounted(fetchUser);

  return {
    profile,
    isLoading,
    error,
  };
}
