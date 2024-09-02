import { Client } from "../types";
import HttpClient from "../utils/httpClient";

export function useClients() {
  const client = new HttpClient();

  async function getClients() {
    const response = await client.get("/clients");
    return response.data as Client[];
  }

  async function createClient(_client: Client) {
    const response = await client.post("/clients", _client);
    return response.data as Client;
  }

  return {
    getClients,
    createClient,
  };
}
