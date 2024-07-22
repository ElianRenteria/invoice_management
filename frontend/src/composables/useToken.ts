// src/composables/useToken.ts
import { useStorage } from "@vueuse/core";
import { useJwt } from "@vueuse/integrations/useJwt";
import { JwtPayload } from "jwt-decode";

export function useToken() {
  const token = useStorage<string | null>("access_token", null);

  const setToken = (newToken: string | null): void => {
    token.value = newToken;
  };

  const getToken = (): string | null => {
    return token.value;
  };

  const decodeToken = (): JwtPayload | null => {
    try {
      return token.value ? useJwt(token.value).payload.value : null;
    } catch (e) {
      console.error("Failed to decode token:", e);
      return null;
    }
  };

  const isTokenExpired = (): boolean => {
    const decoded = decodeToken();
    if (!decoded || !decoded.exp) {
      return true;
    }
    // JWT typically uses seconds since epoch, but JavaScript uses milliseconds
    return decoded.exp * 1000 < Date.now();
  };

  return {
    setToken,
    getToken,
    decodeToken,
    isTokenExpired,
    token, // exposing the reactive token directly might be useful in some scenarios
  };
}
