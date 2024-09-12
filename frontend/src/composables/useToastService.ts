import { useToast } from "primevue/usetoast";

export function useToastService() {
  const toast = useToast();

  function success(message: string) {
    toast.add({ severity: "success", summary: "Success", detail: message });
  }

  function error(message: string) {
    toast.add({ severity: "error", summary: "Error", detail: message });
  }

  function info(message: string) {
    toast.add({ severity: "info", summary: "Info", detail: message });
  }

  function warn(message: string) {
    toast.add({ severity: "warn", summary: "Warning", detail: message });
  }

  return {
    success,
    error,
    info,
    warn,
  };
}
