import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const data = {
  userNotFound: false,
  passwordNoMatch: false,
  loginFlag: false, 
};

const getters = {
  userNotFound: (state) => state.userNotFound,
  passwordNoMatch: (state) => state.passwordNoMatch,
  loginFlag: (state) => state.loginFlag,
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
        // clean this up
        if (res.data.login_flag) {
          commit('session/setUserObject', res.data.user, { root: true })
          commit('setLoginFlag', res.data.login_flag)
          router.push({ path: '/Data' });
        }
        commit('setNoPasswordMatch', res.data.Password_no_match);
        commit('setUserNotFound', res.data.Not_found);
      })
      .catch((error) => {
        console.log(error);
      });
  },

};

const mutations = {

  setUserNotFound(state, value) {
    state.userNotFound = value;
  },

  setNoPasswordMatch(state, value) {
    state.passwordNoMatch = value;
  },

  setLoginFlag(state, value) {
    state.loginFlag = value;
  },

};

export default {
  namespaced: true,
  state: data,
  getters,
  actions,
  mutations,
};
