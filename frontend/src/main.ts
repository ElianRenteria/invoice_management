import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

/**
 * PrimeVue
 */
import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";

/**
 * The main entry point for the Vue.js application.
 */
const app = createApp(App);

/**
 * Vue Router
 */
import router from "./router";
app.use(router);

/**
 * PrimeVue - Configuration
 */
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});

/**
 * PrimeFlex
 */
import "primeflex/primeflex.css";

/**
 * PrimeIcons
 */

import "primeicons/primeicons.css";

/**
 * Mount the Vue.js application to the DOM.
 */
app.mount("#app");
