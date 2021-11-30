import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios'
// import router from '../../router';

Vue.use(Vuex);

const data = {
  userObject: [],
};

const getters = {
  userObject: (state) => state.userObject,
};

const mutations = {

  setUserObject(state, value) {
    state.userObject = value;
  },

};

export default {
  namespaced: true,
  state: data,
  getters,
  // actions,
  mutations,
};
