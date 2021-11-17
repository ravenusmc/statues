import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
// import router from '../../router';

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
        // router.push({ path: '/login' });
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
