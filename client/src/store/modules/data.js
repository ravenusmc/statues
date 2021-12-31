import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	firstGraphDataSetInitial: [
		['Side', 'Count'],
		['South', 1722],
		['Not Applicable', 377],
		['North', 43],
	],
};

const getters = {
	firstGraphDataSetInitial: state => state.firstGraphDataSetInitial,
};

const actions = {

	fetchNorthSouthByYear: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_north_south_by_year';
		axios.post(path, payload)
			.then((res) => {
				res.data.sort((a, b) => b[1] - a[1]);
				commit('setFirstGraphDataSetInitial', res.data)
			})
	},
};


const mutations = {

	setFirstGraphDataSetInitial(state, data) {
		state.firstGraphDataSetInitial = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};