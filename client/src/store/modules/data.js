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
	graphThreeYearOne: 1854,
	graphThreeYearTwo: 2017,
	thirdGraphDataSet: [
		['State', 'South', 'North', 'N/A'],
		['AK', 0, 0, 1]
	],
	removedStatuesData: [
		['Southern State', 'Count'], 
		['TX', 24], 
		['VA', 20], 
		['FL', 11], 
		['TN', 8], 
		['GA', 7]
	],
	// I don't like how I am calling Date here...Not good!!!
	removedStatuesByYearsData: [
		['Year removed', 'Count'], 
		[new Date(2012, 0, 1), 2], 
		[new Date(2013, 0, 1), 1],
		[new Date(2014, 0, 1), 2], 
		[new Date(2015, 0, 1), 15], 
		[new Date(2016, 0, 1), 18], 
		[new Date(2017, 0, 1), 63], 
		[new Date(2018, 0, 1), 32], 
		[new Date(2019, 0, 1), 22], 
		[new Date(2020, 0, 1), 172], 
		[new Date(2021, 0, 1), 23],
	],
	sixthGraphDataSet: [],
};

const getters = {
	firstGraphDataSetInitial: state => state.firstGraphDataSetInitial,
	graphOneYearOne: state => state.graphOneYearOne,
	graphOneYearTwo: state => state.graphOneYearTwo,
	drillDownData: state => state.drillDownData,
	graphTwoYearOne: state => state.graphTwoYearOne,
	graphTwoYearTwo: state => state.graphTwoYearTwo,
	secondGraphDataSetInitial: state => state.secondGraphDataSetInitial,
	graphThreeYearOne: state => state.graphThreeYearOne,
	graphThreeYearTwo: state => state.graphThreeYearTwo,
	thirdGraphDataSet: state => state.thirdGraphDataSet,
	removedStatuesData: state => state.removedStatuesData, 
	removedStatuesByYearsData: state => state.removedStatuesByYearsData,
	sixthGraphDataSet: state => state.sixthGraphDataSet,
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

	fetchStatuesBySingleState: ({ commit }, { payload }) => {
		// Using graph two's year for the drill down graph may or may not be the best option...
		commit('setGraphThreeYearOne', payload.yearOne)
		commit('setGraphThreeYearTwo', payload.yearTwo)
		const path = 'http://localhost:5000/fetch_Statues_Single_State';
		axios.post(path, payload)
			.then((res) => {
				commit('setThirdGraphDataSet', res.data)
			})
	},

	fetchDrillDownDataGraphThree: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_drilldown_graph_three';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
			})
	},

	fetchDrillDownDataGraphFour: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_drilldown_graph_four';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
			})
	},

	fetchDrillDownDataGraphFive: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_drilldown_graph_five';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
			})
	},

	resetDrillDownData: ({ commit }) => {
		let drillDownData = []
		commit('setDrillDownData', drillDownData)
	}

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
		state.drillDownData = data
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

	setGraphThreeYearOne(state, data) {
		state.graphThreeYearOne = data
	},

	setGraphThreeYearTwo(state, data) {
		state.graphThreeYearTwo = data
	},

	setThirdGraphDataSet(state, data) {
		state.thirdGraphDataSet = data
	},

	setGraphThreeYearOne(state, data) {
		state.graphThreeYearOne = data
	},

	setGraphThreeYearTwo(state, data) {
		state.graphThreeYearTwo = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};