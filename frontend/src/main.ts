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
 * PrimeVue - Configuration
 */
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});

/**
 * Mount the Vue.js application to the DOM.
 */
app.mount("#app");
