import { ToastMessageOptions } from "primevue/toast";
import { useToast } from "primevue/usetoast";

export interface PresentToastOptions {
  title?: string;
  duration?: number;
  closable?: boolean;
  sticky?: boolean;
}

export function useToastService() {
  const toast = useToast();

  const defaultOptions: PresentToastOptions = {
    title: undefined,
    duration: 3000,
    closable: true,
    sticky: false,
  };

  /**
   * Displays a toast message with the specified options.
   *
   * @param level - The severity level of the toast message (e.g., 'success', 'info', 'warn', 'error').
   * @param message - The main content of the toast message.
   * @param options - The options for the toast message.
   * @param options.title - The title of the toast message.
   * @param options.duration - The duration of the toast message. Defaults to 3000ms.
   * @param options.closable - Whether the toast message is manually closable. Defaults to true.
   * @param options.sticky - Whether the toast message is sticky. If true, the duration is ignored. Defaults to false.
   */
  function present(
    level: ToastMessageOptions["severity"],
    message: string,
    options: PresentToastOptions = defaultOptions,
  ) {
    const { title, duration, closable, sticky } = {
      ...defaultOptions,
      ...options,
    };
    toast.add({
      severity: level,
      summary: title,
      detail: message,
      life: sticky ? undefined : duration,
      closable: closable,
    });
  }

  return {
    present,
  };
}
