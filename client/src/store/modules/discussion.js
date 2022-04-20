import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const state = {
  graph_discussion_points: [],
};

const getters = {
  graph_discussion_points: (state) => state.graph_discussion_points,
};

const actions = {

  getDisscusionData: ({ commit }, { payload }) => {
    router.push({ name: 'SpecificDiscussionPage' });
    const path = 'http://localhost:5000/get_specific_discussion_data';
    axios.post(path, payload)
      .then((res) => {
        commit('setGraph_discussion_points', res.data)
      })
      .catch((error) => {
        console.log(error);
      });
   },

};

const mutations = {

  setGraph_discussion_points(state, data) {
    state.graph_discussion_points = data;
  },

};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};