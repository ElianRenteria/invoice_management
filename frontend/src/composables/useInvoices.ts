import { Invoice } from "../types";
import HttpClient from "../utils/httpClient";

export function useInvoices() {
  const client = new HttpClient();

  async function getInvoices() {
    const response = await client.get("/invoices");
    return response.data as Invoice[];
  }

  async function createInvoices(_invoice: Invoice) {
    const response = await client.post("/invoices", _invoice);
    return response.data as Invoice;
  }

  return {
    getInvoices,
    createInvoices,
  };
}