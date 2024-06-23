// src/utils/httpClient.ts
import axios, { AxiosInstance, AxiosResponse } from "axios";
import router from "@/router"; // Import Vue router if you're using Vue Router

class HttpClient {
  private readonly instance: AxiosInstance;

  constructor(baseURL: string) {
    this.instance = axios.create({
      baseURL: baseURL,
      headers: {
        "Content-Type": "application/json",
      },
    });

    this.initializeRequestInterceptor();
    this.initializeResponseInterceptor();
  }

  private initializeRequestInterceptor(): void {
    this.instance.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem("access_token");
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );
  }

  private initializeResponseInterceptor(): void {
    this.instance.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response && error.response.status === 401) {
          // Handle 401 error specifically here
          // Redirect to login or handle session timeout
          router.push("/login").catch((err) => {
            console.error("Router navigation error:", err);
          });
        }
        return Promise.reject(error);
      }
    );
  }

  public get<T>(url: string, params?: any): Promise<AxiosResponse<T, any>> {
    return this.instance.get<T>(url, { params });
  }

  public post<T>(url: string, data?: any): Promise<AxiosResponse<T, any>> {
    return this.instance.post<T>(url, data);
  }

  public put<T>(url: string, data?: any): Promise<AxiosResponse<T, any>> {
    return this.instance.put<T>(url, data);
  }

  public delete<T>(url: string, params?: any): Promise<AxiosResponse<T, any>> {
    return this.instance.delete<T>(url, { params });
  }
}

// Usage example:
const apiClient = new HttpClient("http://localhost:8080");
export default apiClient;
