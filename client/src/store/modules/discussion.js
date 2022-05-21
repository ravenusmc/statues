import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const state = {
  selectedGraph: 1,
  graph_discussion_points: [],
  showDiscussion: true,
};

const getters = {
  selectedGraph: (state) => state.selectedGraph,
  graph_discussion_points: (state) => state.graph_discussion_points,
  showDiscussion: (state) => state.showDiscussion,
};

const actions = {

  getDisscusionData: ({ commit }, { payload }) => {
    commit('setSelectedGraph', payload.selectedGraphDiscussion)
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

  addDisscusionPost: ({ commit }, { payload }) => {
    const path = 'http://localhost:5000/add_discussion_post';
    axios.post(path, payload)
      .then((res) => {
        commit('setGraph_discussion_points', res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },

  deleteDisscusionPost: ({ commit }, { payload }) => {
    const path = 'http://localhost:5000/delete_discussion_post';
    axios.post(path, payload)
      .then((res) => {
        commit('setGraph_discussion_points', res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },

  switchDiscussionOrdering: ({ commit }, { payload }) => {
    const path = 'http://localhost:5000/switch_discussion_posts';
    axios.post(path, payload)
      .then((res) => {
        commit('setGraph_discussion_points', res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },

  changeDiscussionVotes: ({ commit }, { payload }) => {
    const path = 'http://localhost:5000/update_discussion_votes';
    axios.post(path, payload)
      .then((res) => {
        commit('setGraph_discussion_points', res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },

  changeBetweenDiscussionAndGraph: ({ commit }, { payload }) => {
    commit('setShowDiscussion', payload['show'])
    if (typeof payload['selectedGraph'] !== 'undefined') {
      const path = 'http://localhost:5000/build_discussion_graph';
      axios.post(path, payload)
        .then((res) => {
          // commit('setGraph_discussion_points', res.data)
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }

};

const mutations = {

  setSelectedGraph(state, data) {
    state.selectedGraph = data;
  },

  setGraph_discussion_points(state, data) {
    state.graph_discussion_points = data;
  },

  setShowDiscussion(state, data) {
    state.showDiscussion = data
  },

};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};