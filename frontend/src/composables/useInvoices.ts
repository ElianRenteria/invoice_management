// src/composables/useInvoices.ts
import { ref, onMounted } from "vue";
import apiClient from "@/services/http_client";

export function useInvoices() {
  const invoices = ref([]);
  const isLoading = ref(false);
  const error = ref<any>(null);

  const fetchInvoices = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      // TODO: Change the return type to Invoice[] once a type is defined
      const response = await apiClient.get<any>("/invoices");
      invoices.value = response.data;
    } catch (err) {
      error.value = err;
    } finally {
      isLoading.value = false;
    }
  };

  const addInvoice = async (invoiceData: any) => {
    isLoading.value = true;
    try {
      await apiClient.post("/invoices", invoiceData);
      await fetchInvoices(); // Refresh the list after adding
    } catch (err) {
      error.value = err;
    } finally {
      isLoading.value = false;
    }
  };

  const updateInvoice = async (id: string, invoiceData: any) => {
    isLoading.value = true;
    try {
      await apiClient.put(`/invoices/${id}`, invoiceData);
      await fetchInvoices(); // Refresh the list after updating
    } catch (err) {
      error.value = err;
    } finally {
      isLoading.value = false;
    }
  };

  const deleteInvoice = async (id: string) => {
    isLoading.value = true;
    try {
      await apiClient.delete(`/invoices/${id}`);
      await fetchInvoices(); // Refresh the list after deleting
    } catch (err) {
      error.value = err;
    } finally {
      isLoading.value = false;
    }
  };

  // Automatically fetch invoices when the component using this composable is mounted
  onMounted(fetchInvoices);

  return {
    invoices,
    isLoading,
    error,
    fetchInvoices,
    addInvoice,
    updateInvoice,
    deleteInvoice,
  };
}
