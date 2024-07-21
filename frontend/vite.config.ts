import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

/**
 * The unplugin-vue-components library can automatically import and register
 * PrimeVue components with the help of @primevue/auto-import-resolver
 */
import Components from "unplugin-vue-components/vite";
import { PrimeVueResolver } from "@primevue/auto-import-resolver";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [PrimeVueResolver()],
    }),
  ],
});
