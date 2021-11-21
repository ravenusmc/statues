import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const state = {
};

const getters = {
};

const actions = {

  setUpUser: (context, { payload }) => {
    const path = 'http://localhost:5000/signup';
    axios.post(path, payload)
      .then((res) => {
        console.log(res.data);
        router.push({ path: '/login' });
      })
      .catch((error) => {
        console.log(error);
      });
  },

  login: ({ commit }, { payload }) => {
    const path = 'http://localhost:5000/login';
    axios.post(path, payload)
      .then((res) => {
        console.log(res.data);
        commit('setNotFound', res.data);
        // if (res.data.login_flag) {
        //   commit('session/setUserObject', res.data.user, { root: true })
        //   commit('setLoginFlag', res.data.login_flag)
        //   router.push({ path: '/set_up' });
        // }
        // commit('setNoPasswordMatch', res.data.Password_no_match)
        // commit('setNotFound', res.data.Not_found)
      })
      .catch((error) => {
        console.log(error);
      });
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