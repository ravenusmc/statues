import Vue from 'vue';
import VueRouter from 'vue-router';
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
    component: () => import('../views/About.vue'),
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
  {
    path: '/discussion',
    name: 'Discussion',
    component: () => import('../views/Discussion.vue'),
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
  {
    path: '/SpecificDiscussionPage',
    name: 'SpecificDiscussionPage',
    component: () => import('../views/SpecificDiscussionPage.vue'),
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
