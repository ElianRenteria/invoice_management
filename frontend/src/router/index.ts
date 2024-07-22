import {
  createMemoryHistory,
  createRouter,
  createWebHashHistory,
  createWebHistory,
  RouteRecordRaw,
} from "vue-router";
import { useToken } from "../composables/useToken";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Dashboard",
    component: () => import("../views/private/Dashboard.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/public/auth/LoginView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
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
