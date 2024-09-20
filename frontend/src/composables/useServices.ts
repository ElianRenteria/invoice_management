import { useToastService } from "./useToastService";
import { Service } from "../types/Service";
import HttpClient from "../utils/httpClient";

export function useServices() {
  const client = new HttpClient();
  const toast = useToastService();

  async function getServices() {
    try {
      const response = await client.get("/services/");
      if (response.status !== 200) {
        throw new Error("Failed to load services.");
      }
      return response.data as Service[];
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Load Failed",
      });
    }
  }

  async function createService(_service: Service) {
    try {
      const response = await client.post("/services/", _service);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_service.name} ${response.status === 200 ? "created successfully" : "failed to create"}.`,
        {
          title:
            response.status === 200 ? "Creation Successful" : "Creation Failed",
        },
      );
      return response.data as Service;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Creation Failed",
      });
    }
  }

  async function updateService(_service: Service) {
    try {
      const response = await client.put(`/services/${_service.id}`, _service);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_service.name} ${response.status === 200 ? "updated successfully" : "failed to update"}.`,
        {
          title:
            response.status === 200 ? "Update Successful" : "Update Failed",
        },
      );
      return response.data as Service;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Update Failed",
      });
    }
  }

  async function deleteService(_service: Service) {
    try {
      const response = await client.delete(`/services/${_service.id}`);
      toast.present(
        response.status === 200 ? "success" : "error",
        `${_service.name} ${response.status === 200 ? "deleted successfully" : "failed to delete"}.`,
        {
          title:
            response.status === 200 ? "Deletion Successful" : "Deletion Failed",
        },
      );
      return response.status === 200;
    } catch (error: Error | any) {
      toast.present("error", error, {
        title: "Deletion Failed",
      });
    }
  }

  return {
    getServices,
    createService,
    updateService,
    deleteService,
  };
}
