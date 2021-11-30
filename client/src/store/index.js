import Vue from 'vue';
import Vuex from 'vuex';
import common from './modules/common';
import session from './modules/session';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    common,
    session,
  },
});
