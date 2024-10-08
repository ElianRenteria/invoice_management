import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { useToken } from "../composables/useToken";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: () => import("../layouts/PrivateLayout.vue"),
    children: [
      {
        path: "",
        name: "Dashboard",
        components: {
          default: () => import("../views/private/DashboardView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "clients",
        name: "Clients",
        components: {
          default: () => import("../views/private/ClientsView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "invoices",
        name: "Invoices",
        components: {
          default: () => import("../views/private/InvoicesView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "services",
        name: "Services",
        components: {
          default: () => import("../views/private/ServicesView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "profile",
        name: "Profile",
        components: {
          default: () => import("../views/private/ProfileView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "settings",
        name: "Settings",
        components: {
          default: () => import("../views/private/SettingView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
      {
        path: "logout",
        name: "Logout",
        components: {
          default: () => import("../views/private/LogoutView.vue"),
          sidebar: () => import("../components/layout/Sidebar.vue"),
        },
      },
    ],
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/public/auth/LoginView.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../views/public/auth/RegisterView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _, next) => {
  // If the route does not require authentication, then allow
  // the user to navigate to it
  if (to.matched.some((record) => record.meta.requiresAuth) === false) {
    next();
    return;
  }

  // If the route requires authentication, then check if the token
  // is expired. If it is expired, then redirect the user to the login
  // page. Otherwise, allow the user to navigate to the route

  if (to.matched.some((record) => record.meta.requiresAuth) === true) {
    const tokenRef = useToken();
    const isTokenExpired = tokenRef.isTokenExpired();
    if (isTokenExpired) {
      next("/login");
    } else {
      next();
    }
  }
});

export default router;
