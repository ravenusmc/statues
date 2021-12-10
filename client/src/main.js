import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faUserSecret, faHashtag, faPencilAlt, faCodeBranch, faNetworkWired,
} from '@fortawesome/free-solid-svg-icons';
import App from './App.vue';
import router from './router';
import store from './store';
import VueGoogleCharts from 'vue-google-charts';

library.add(faUserSecret,
  faHashtag,
  faPencilAlt,
  faCodeBranch,
  faNetworkWired);

Vue.component('fa-icon', FontAwesomeIcon);

// Google charts plugin
Vue.use(VueGoogleCharts);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
