import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const state = {
  // userNotFound: false,
};

const getters = {
  // userNotFound: (state) => state.userNotFound,
};

const actions = {

  getDisscusionData: ({ commit }, { payload }) => {
		router.push({ name: 'SpecificDiscussionPage' });
  //   const path = 'http://localhost:5000/get_specific_discussion_data';
  //   axios.post(path, payload)
  //     .then((res) => {
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
   },

};

const mutations = {

  // setUserNotFound(state, value) {
  //   state.userNotFound = value;
  // },

};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};