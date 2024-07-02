import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LogInView from "../views/LogInView.vue";
import SignUpView from "../views/SignUpView.vue";
import DashboardView from "../views/DashboardView.vue";
import ClientsView from "../views/ClientsView.vue";
import InvoicesView from "../views/InvoicesView.vue";
import ServicesView from "../views/ServicesView.vue";
import SettingsView from "../views/SettingsView.vue";
import AboutView from "../views/AboutView.vue";

const routes: Array<RouteRecordRaw> = [
  // Example if we want to load things on request to make web bundle smaller
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () =>
    //  import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: LogInView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUpView,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: "/clients",
    name: "clients",
    component: ClientsView,
    meta: { requiresAuth: true },
  },
  {
    path: "/invoices",
    name: "invoices",
    component: InvoicesView,
    meta: { requiresAuth: true },
  },
  {
    path: "/services",
    name: "services",
    component: ServicesView,
    meta: { requiresAuth: true },
  },
  {
    path: "/settings",
    name: "settings",
    component: SettingsView,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import("../views/LogInView.vue"),
  },
  {
    path: "/signup",
    name: "signup",
    component: () =>
      import("../views/SignUpView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});


router.beforeEach((to, from, next) => {

  const token = localStorage.getItem("authToken");
  const isAuthenticated = true;//!!token;

  if (to.matched.some((record) => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: "login" });
  } 
  else if (isAuthenticated && ((to.name === 'login') || (to.name === 'signup') || (to.name === 'home'))) {
    next({ name: 'dashboard' });
  } 
  else {
    next();
  }
});



export default router;
