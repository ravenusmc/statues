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
	drillDownData: [],
	graphTwoYearOne: 1854,
	graphTwoYearTwo: 2017,
	secondGraphDataSetInitial: [
		['State', 'Count'], 
		['VA', 221], 
		['TX', 159], 
		['GA', 135], 
		['NC', 112], 
		['AL', 92]
	],
};

const getters = {
	firstGraphDataSetInitial: state => state.firstGraphDataSetInitial,
	graphOneYearOne: state => state.graphOneYearOne,
	graphOneYearTwo: state => state.graphOneYearTwo,
	drillDownData: state => state.drillDownData,
	graphTwoYearOne: state => state.graphTwoYearOne,
	graphTwoYearTwo: state => state.graphTwoYearTwo,
	secondGraphDataSetInitial: state => state.secondGraphDataSetInitial,
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
				commit('setDrillDownData', res.data)
			})
	},

	fetchTopFiveByYear: ({ commit }, { payload }) => {
		commit('setGraphTwoYearOne', payload.yearOne)
		commit('setGraphTwoYearTwo', payload.yearTwo)
		const path = 'http://localhost:5000/fetch_top_five_by_year';
		axios.post(path, payload)
			.then((res) => {
				commit('setSecondGraphDataSetInitial', res.data)
			})
	},

	fetchDrillDownDataGraphTwo: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_north_south_by_state_drilldown';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
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

	setDrillDownData(state, data) {
		state.drillDownData= data
	},

	setGraphTwoYearOne(state, data) {
		state.graphTwoYearOne = data
	},

	setGraphTwoYearTwo(state, data) {
		state.graphTwoYearTwo = data
	},

	setSecondGraphDataSetInitial(state, data) {
		state.secondGraphDataSetInitial = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};