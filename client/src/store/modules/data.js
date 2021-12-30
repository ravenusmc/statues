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
				console.log(res.data)
				// commit('setGraphTwoData', res.data)
			})
	},
};


const mutations = {

	setColumns(state, data) {
		state.columns = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};