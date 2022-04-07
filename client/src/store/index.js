import Vue from 'vue';
import Vuex from 'vuex';
import common from './modules/common';
import session from './modules/session';
import data from './modules/data';
import discussion from './modules/discussion';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    common,
    session,
    data,
    discussion,
  },
});
