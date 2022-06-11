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
	sixthGraphDataSet: [
		['Symbol Type', 'Count'],
		['Monument', 115],
		['Other', 54],
		['School', 31],
		['Building', 19],
		['County/Municipality', 2],
	],
	sixthGraphSelectedState: 'VA',
	sixthGraphSixYearOne: 1854,
	sixthGraphSixYearTwo: 2017,
	mapData: [
		['State', 'Total Monuments'],
		['US-AZ', 0],
		['US-TX', 1],
		['US-GA', 0],
		['US-TN', 0],
		['US-FL', 0],
		['US-CA', 0],
		['US-DC', 0],
		['US-DE', 0],
		['US-NC', 0],
		['US-MS', 1],
		['US-VA', 0],
		['US-AR', 0],
		['US-IA', 0],
		['US-WA', 0],
		['US-SC', 0],
		['US-KY', 0],
		['US-WV', 0],
		['US-AL', 0],
		['US-NM', 0],
		['US-MT', 0],
		['US-NY', 0],
		['US-MD', 0],
		['US-OH', 0],
		['US-IN', 0],
		['US-OR', 0],
		['US-MA', 0],
		['US-SD', 0],
		['US-ME', 0],
		['US-KS', 0],
		['US-UT', 0],
		['US-NV', 0],
		['US-AK', 0]
	],
	mapYear: 1854
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
	sixthGraphSelectedState: state => state.sixthGraphSelectedState,
	sixthGraphSixYearOne: state => state.sixthGraphSixYearOne,
	sixthGraphSixYearTwo: state => state.sixthGraphSixYearTwo,
	mapData: state => state.mapData,
	mapYear: state => state.mapYear,
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
	},

	fetchDataForSixthGraph: ({ commit }, { payload }) => {
		commit('setGraphSixYearOne', payload.yearOne)
		commit('setGraphSixYearTwo', payload.yearTwo)
		commit('setSixthGraphSelectedState', payload.state)
		const path = 'http://localhost:5000/fetch_data_for_graph_six';
		axios.post(path, payload)
			.then((res) => {
				res.data.sort((a, b) => b[1] - a[1]);
				commit('setSixthGraphDataSet', res.data)
			})
	},

	fetchDrillDownDataGraphSix: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_drilldown_graph_six';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
			})
	},

	fetchMapData: ({ commit }, { payload }) => {
		console.log('Action')
		console.log(payload)
		// commit('setMapYear', )
		const path = 'http://localhost:5000/fetch_map_data';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setDrillDownData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	// This action sets the drill down data for the sentiment graph
	fetchSentimentDrillDownData: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetch_sentiment_drilldown_data';
		axios.post(path, payload)
			.then((res) => {
				commit('setMapData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
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

	setSixthGraphDataSet(state, data) {
		state.sixthGraphDataSet = data
	},

	setSixthGraphSelectedState(state, data) {
		state.sixthGraphSelectedState = data
	},

	setGraphSixYearOne(state, data) {
		state.sixthGraphSixYearOne = data
	},

	setGraphSixYearTwo(state, data) {
		state.sixthGraphSixYearTwo = data
	},

	setMapData(state, data) {
		state.mapData = data
	},

	setMapYear(state, data) {
		state.mapYear = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};