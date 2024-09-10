import { Service } from "../types/Service";
import HttpClient from "../utils/httpClient";

export function useServices() {
  const client = new HttpClient();

  async function getServices() {
    const response = await client.get("/services/");
    return response.data as Service[];
  }

  async function createService(_service: Service) {
    const response = await client.post("/services/", _service);
    return response.data as Service;
  }

  async function updateService(_service: Service) {
    const response = await client.put(`/services/${_service.id}`, _service);
    return response.data as Service;
  }

  async function deleteService(_service: Service) {
    const response = await client.delete(`/services/${_service.id}`, _service);
    return response.data as Service;
  }

  return {
    getServices,
    createService,
    updateService,
    deleteService,
  };
}
