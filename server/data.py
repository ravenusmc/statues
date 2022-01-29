# This file will deal with a lot of the data analysis for this project.

# importing supporting libraries
import numpy as np
import pandas as pd
from datetime import datetime

# Files that I built
from clean import *


class Data():

    def build_north_south_graph(self, years):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        yearOne = years['yearOne']
        yearTwo = years['yearTwo']
        statues_data_set_by_year = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (
            statues_data_subset['Year Dedicated'] <= yearTwo)]
        first_chart_data = []
        columns = ['Side', 'Count']
        first_chart_data.append(columns)
        sides = ['North', 'South', 'Not Applicable']
        for side in sides:
            rows = []
            number_of_statues = len(
                statues_data_set_by_year[(statues_data_subset.Side == side)])
            rows.append(side)
            rows.append(number_of_statues)
            first_chart_data.append(rows)
        return first_chart_data

    def build_north_south_graph_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        yearOne = post_data['graphOneYearOne']
        yearTwo = post_data['graphOneYearTwo']
        side = post_data['side']
        statues_data_set_by_year_drill_down = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (
            statues_data_subset['Year Dedicated'] <= yearTwo) & (statues_data_subset['Side'] == side)]
        return statues_data_set_by_year_drill_down

    def build_top_five_graph(self, years):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        yearOne = years['yearOne']
        yearTwo = years['yearTwo']
        statues_data_set_by_year = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (
            statues_data_subset['Year Dedicated'] <= yearTwo)]
        state_counts = statues_data_set_by_year['State'].value_counts().head(5)
        second_chart_data = []
        columns = ['State', 'Count']
        second_chart_data.append(columns)
        count = 0
        for state in state_counts.to_frame().index:
            rows = []
            rows.append(state)
            rows.append(int(state_counts.iloc[count]))
            second_chart_data.append(rows)
            count += 1
        return second_chart_data

    def build_graph_two_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        drilldown_data_graph_two = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_two.append(columns)
        yearOne = post_data['graphTwoYearOne']
        yearTwo = post_data['graphTwoYearTwo']
        state = post_data['state']
        statues_data_set_by_year_drill_down_two = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (
            statues_data_subset['Year Dedicated'] <= yearTwo) & (statues_data_subset['State'] == state)]
        return statues_data_set_by_year_drill_down_two 

