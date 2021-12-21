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

	// fetchFileInformation: ({ commit }, { formData }) => {
	// 	const path = 'http://localhost:5000/fetch_File_Information';
	// 	axios.post(path, formData, {
	// 		headers: {
	// 			'Content-Type': 'multipart/form-data'
	// 		}
	// 	})
	// 		.then((res) => {
	// 			commit('setFileName', res.data.file_name)
	// 			commit('setColumns', res.data.column_names)
	// 			commit('setShowDataArea', true)
	// 		})
	// 		.catch(error => {
	// 			console.log(error);
	// 		})
	// },

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