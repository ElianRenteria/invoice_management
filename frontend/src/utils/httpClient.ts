// src/utils/httpClient.ts
import APIConfig from "../config/APIConfig";
import axios, { AxiosInstance, AxiosResponse } from "axios";
import { useRouter } from "vue-router";
import { useToken } from "../composables/useToken";

export default class HttpClient {
  private readonly instance: AxiosInstance;
  private readonly router = useRouter();
  private readonly tokenRef = useToken();

  constructor() {
    this.instance = axios.create({
      baseURL: APIConfig.baseURL(),
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
        const token = this.tokenRef;
        if (!token.isTokenExpired()) {
          config.headers.Authorization = `Bearer ${token.getToken()}`;
          return config;
        }
        console.error("[HttpClient :: Request Interceptor] Token expired");
        // Redirect to login or handle session timeout
        this.router.push("/login").catch((err) => {
          console.error("Router navigation error:", err);
        });
        return Promise.reject("Token expired");
      },
      (error) => {
        return Promise.reject(error);
      },
    );
  }

  private initializeResponseInterceptor(): void {
    this.instance.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response && error.response.status === 401) {
          // Handle 401 error specifically here
          console.error("[HttpClient :: Response Interceptor] Token expired");
          // Redirect to login or handle session timeout
          this.router.push("/login").catch((err) => {
            console.error("Router navigation error:", err);
          });
        }
        return Promise.reject(error);
      },
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
