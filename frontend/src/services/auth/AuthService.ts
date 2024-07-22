import APIConfig from "../../config/APIConfig";
import axios, { AxiosInstance } from "axios";

export default class AuthService {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: APIConfig.baseURL(),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async login(email: string, password: string) {
    return this.client.post("/auth/login", {
      email,
      password,
    });
  }

  // TODO: Implement Backend Logic to Make This Endpoint Functional
  async logout() {
    return this.client.post("/auth/logout");
  }

  async register(
    email: string,
    password: string,
    first_name: string,
    last_name: string,
  ) {
    return this.client.post("/auth/signup", {
      email,
      password,
      first_name,
      last_name,
    });
  }
}
