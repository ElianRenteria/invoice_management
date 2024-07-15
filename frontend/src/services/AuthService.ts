import axios, { AxiosInstance } from "axios";
class AuthService {
  private client: AxiosInstance;

  constructor(baseURL: string) {
    this.client = axios.create({
      baseURL: baseURL,
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async login(email: string, password: string) {
    return await this.client.post("/login", {
      email,
      password,
    });
  }

  // TODO: Backend Implementation of Invalidating Previously Issued JWT Tokens
  async logout() {
    return await this.client.post("/logout");
  }

  async register(
    email: string,
    password: string,
    first_name: string,
    last_name: string
  ) {
    return await this.client.post("/signup", {
      email,
      password,
      first_name,
      last_name,
    });
  }
}

const authService = new AuthService("http://localhost:8080/api/v1/auth");
export default authService;
