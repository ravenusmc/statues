import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios'
// import router from '../../router';

Vue.use(Vuex);

const state = {
};

const getters = {
};

const actions = {

  setUpUser: ({ payload }) => {
    console.log(payload);
  },

};

const mutations = {

};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
