import { useToastService } from "./useToastService";
import { Client } from "../types";
import HttpClient from "../utils/httpClient";

export function useClients() {
  const client = new HttpClient();
  const toast = useToastService();

  async function getClients() {
    try {
      const response = await client.get("/clients/");
      if (response.status !== 200) {
        throw new Error("Failed to load clients.");
      }
      return response.data as Client[];
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Load Failed",
      });
    }
  }

  async function createClient(_client: Client) {
    try {
      const response = await client.post("/clients/", _client);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_client.name} ${response.status === 200 ? "created successfully" : "failed to create"}.`,
        {
          title:
            response.status === 200 ? "Creation Successful" : "Creation Failed",
        },
      );
      return response.data as Client;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Creation Failed",
      });
    }
  }

  async function updateClient(_client: Client) {
    try {
      const response = await client.put(`/clients/${_client.id}`, _client);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_client.name} ${response.status === 200 ? "updated successfully" : "failed to update"}.`,
        {
          title:
            response.status === 200 ? "Update Successful" : "Update Failed",
        },
      );
      return response.data as Client;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Update Failed",
      });
    }
  }

  async function deleteClient(_client: Client) {
    try {
      const response = await client.delete(`/clients/${_client.id}`);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_client.name} ${response.status === 200 ? "deleted successfully" : "failed to delete"}.`,
        {
          title:
            response.status === 200 ? "Deletion Successful" : "Deletion Failed",
        },
      );
      return response.data as Client;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Deletion Failed",
      });
    }
  }

  return {
    getClients,
    createClient,
    updateClient,
    deleteClient,
  };
}
