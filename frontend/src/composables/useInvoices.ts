import { useToastService } from "./useToastService";
import { Invoice } from "../types";
import HttpClient from "../utils/httpClient";

export function useInvoices() {
  const client = new HttpClient();
  const toast = useToastService();

  async function getInvoices() {
    try {
      const response = await client.get("/invoices");
      if (response.status !== 200) {
        throw new Error("Failed to load invoices.");
      }
      return response.data as Invoice[];
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Load Failed",
      });
    }
  }

  async function createInvoices(_invoice: Invoice) {
    /**
     * TODO: TOAST FUNCTIONALITY
     * Implement toast messages for success and error cases.
     * Use the `toast.present` function from the `useToastService` composable.
     * Invoice type must be implemented prior to toast implementation.
     * Currently, the Invoice type is defined, but not implemented.
     */

    const response = await client.post("/invoices", _invoice);
    return response.data as Invoice;
  }

  return {
    getInvoices,
    createInvoices,
  };
}
