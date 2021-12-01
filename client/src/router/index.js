import Vue from 'vue';
import VueRouter from 'vue-router';
// import store from '../store/index.js';
import store from '@/store/index';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/sign_up',
    name: 'signup',
    component: () => import('../views/SignUp.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue'),
  },
  {
    path: '/data',
    name: 'Data',
    component: () => import('../views/Data.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
