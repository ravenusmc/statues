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
	graphOneYearOne: 1854,
	graphOneYearTwo: 2017,
	drillDownDataGraphOne: [],
	graphTwoYearOne: 1854,
	graphTwoYearTwo: 2017,
};

const getters = {
	firstGraphDataSetInitial: state => state.firstGraphDataSetInitial,
	graphOneYearOne: state => state.graphOneYearOne,
	graphOneYearTwo: state => state.graphOneYearTwo,
	drillDownDataGraphOne: state => state.drillDownDataGraphOne,
	graphTwoYearOne: state => state.graphTwoYearOne,
	graphTwoYearTwo: state => state.graphTwoYearTwo,
};

const actions = {

	fetchNorthSouthByYear: ({ commit }, { payload }) => {
		commit('setGraphOneYearOne', payload.yearOne)
		commit('setGraphOneYearTwo', payload.yearTwo)
		const path = 'http://localhost:5000/fetch_north_south_by_year';
		axios.post(path, payload)
			.then((res) => {
				res.data.sort((a, b) => b[1] - a[1]);
				commit('setFirstGraphDataSetInitial', res.data)
			})
	},

	fetchDrillDownDataGraphOne: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_north_south_by_year_drilldown';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setDrillDownDataGraphOne', res.data)
			})
	},

	fetchTopFiveByYear: ({ commit }, { payload }) => {
		commit('setGraphTwoYearOne', payload.yearOne)
		commit('setGraphTwoYearTwo', payload.yearTwo)
		console.log('ACTION!!')
		console.log(payload)
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

	setGraphOneYearOne(state, data) {
		state.graphOneYearOne = data
	},

	setGraphOneYearTwo(state, data) {
		state.graphOneYearTwo = data
	},

	setDrillDownDataGraphOne(state, data) {
		state.drillDownDataGraphOne = data
	},

	setGraphTwoYearOne(state, data) {
		state.graphTwoYearOne = data
	},

	setGraphTwoYearTwo(state, data) {
		state.graphTwoYearTwo = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};