import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/aura-light-blue/theme.css";
import "primeicons/primeicons.css";
import Ripple from "primevue/ripple";
import Menu from "primevue/menu";
import ProgressSpinner from "primevue/progressspinner";

const app = createApp(App);
app.use(PrimeVue, { ripple: true });
app.use(store);
app.use(router);
app.component("PrimeMenu", Menu);
app.component("ProgressSpinner", ProgressSpinner);
app.directive("ripple", Ripple);
app.mount("#app");
