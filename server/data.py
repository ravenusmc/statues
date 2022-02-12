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

    def build_top_five_graph(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        yearOne = statues_data_subset['Year Dedicated'] >= post_data['yearOne']
        yearTwo = statues_data_subset['Year Dedicated'] <= post_data['yearTwo']
        statues_data_set_by_year = statues_data_subset[(yearOne) & (yearTwo)]
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

    def build_singe_state_graph(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        state = statues_data_subset['State'] == post_data['state']
        yearOne = statues_data_subset['Year Dedicated'] >= post_data['yearOne']
        yearTwo = statues_data_subset['Year Dedicated'] <= post_data['yearTwo']
        statues_data_set_by_state = statues_data_subset[(state) &
                                                        (yearOne) & (yearTwo)]
        third_chart_data = []
        columns = ['State', 'North', 'South', 'N/A or Blank']
        third_chart_data.append(columns)
        rows = []
        rows.append(post_data['state'])
        # Count for North
        North = statues_data_set_by_state['Side'] == 'North'
        North_Count = len(statues_data_set_by_state[North])
        rows.append(North_Count)
        # Count for South
        South = statues_data_set_by_state['Side'] == 'South'
        South_count = len(statues_data_set_by_state[South])
        rows.append(South_count)
        # Count for Not Applicable
        Not_Applicable = statues_data_set_by_state['Side'] == 'Not Applicable'
        Not_Applicable_Count = len(statues_data_set_by_state[Not_Applicable])
        # Count for Blank
        Blank = statues_data_set_by_state['Side'].isnull()
        Blank_count = len(statues_data_set_by_state[Blank])
        rows.append(Not_Applicable_Count + Blank_count)
        third_chart_data.append(rows)
        return third_chart_data

    def build_graph_three_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        drilldown_data_graph_two = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_two.append(columns)
        # Setting up the filtering - I like this way better which I learned from Colt Steele
        state = statues_data_subset['State'] == post_data['state']
        yearOne = statues_data_subset['Year Dedicated'] >= post_data['graphThreeYearOne']
        yearTwo = statues_data_subset['Year Dedicated'] <= post_data['graphThreeYearTwo']
        if post_data['side_selected'] == 'N/A or Blank':
            Not_Applicable = statues_data_subset['Side'] == 'Not Applicable'
            Blank = statues_data_subset['Side'].isnull()
            frames = [Not_Applicable, Blank]
            side = pd.concat(frames)
            print('HERE')
            print(side.index.duplicated())
            input()
        else:
            side = statues_data_subset['Side'] == post_data['side_selected']
        statues_data_drill_down_three = statues_data_subset[(state) &
                                                        (yearOne) & (yearTwo) & (side)]
        return statues_data_drill_down_three
