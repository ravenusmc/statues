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
        if (post_data['side_selected'] == 'N/A') or (post_data['side_selected'] == 'N/A or Blank'):
            side = statues_data_subset['Side'] == 'Not Applicable'
            not_applicable_statues = statues_data_subset[(state) &
                                                         (yearOne) & (yearTwo) & (side)]
            side_is_null = statues_data_subset['Side'].isnull()
            is_null_statues = statues_data_subset[(state) &
                                                  (yearOne) & (yearTwo) & (side_is_null)]
            statues_data_drill_down_three = pd.concat(
                [not_applicable_statues, is_null_statues])
        else:
            side = statues_data_subset['Side'] == post_data['side_selected']
            statues_data_drill_down_three = statues_data_subset[(state) &
                                                                (yearOne) & (yearTwo) & (side)]
        return statues_data_drill_down_three

    def build_graph_four_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        drilldown_data_graph_two = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_two.append(columns)
        state = statues_data_subset['State'] == post_data['state']
        removed = statues_data_subset['Removed After Charlottesville'] == 1
        statues_data_drill_down_four = statues_data_subset[(state) & (removed)]
        return statues_data_drill_down_four

    def build_graph_five_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        drilldown_data_graph_five = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_five.append(columns)
        year_removed_data = statues_data_subset['Year Removed'] == post_data['year']
        statues_data_drill_down_five = statues_data_subset[(year_removed_data)]
        return statues_data_drill_down_five

    def build_graph_six_data(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        state = statues_data_subset['State'] == post_data['state']
        yearOne = statues_data_subset['Year Dedicated'] >= post_data['yearOne']
        yearTwo = statues_data_subset['Year Dedicated'] <= post_data['yearTwo']
        statues_data_set_for_symbol_type = statues_data_subset[(state) &
                                                               (yearOne) & (yearTwo)]
        sixth_chart_data = []
        columns = ['Symbol Type', 'Count']
        sixth_chart_data.append(columns)
        symbol_types = ['Monument', 'Roadway', 'County/Municipality', 'Building', 'School',
                        'Roads', 'Highway / Roadway', 'Other']
        for symbol_type in symbol_types:
            rows = []
            number_of_symbol_types = len(
                statues_data_set_for_symbol_type[(statues_data_set_for_symbol_type['Symbol Type'] == symbol_type)])
            if number_of_symbol_types != 0:
                rows.append(symbol_type)
                rows.append(number_of_symbol_types)
                sixth_chart_data.append(rows)
        return sixth_chart_data

    def build_graph_six_drill_down(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        drilldown_data_graph_six = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_six.append(columns)
        symbol_type = statues_data_subset['Symbol Type'] == post_data['selectedSymbol']
        state = statues_data_subset['State'] == post_data['state']
        yearOne = statues_data_subset['Year Dedicated'] >= post_data['graphsixYearOne']
        yearTwo = statues_data_subset['Year Dedicated'] <= post_data['graphSixYearTwo']
        statues_data_drill_down_six = statues_data_subset[(symbol_type) & (state) & (yearOne) &
                                                          (yearTwo)]
        return statues_data_drill_down_six

    def get_sentiment_data(self, graph_discussion_points):
        count = 0
        sentiment_values_array = []
        while count < len(graph_discussion_points):
            sentiment_values_array.append(graph_discussion_points[count][4])
            count += 1
        return sentiment_values_array

    def build_relationship_between_count_and_discussion_point(self, graph_discussion_points):
        count_and_discussion_point_relationship = {}
        count = 0
        while count < len(graph_discussion_points):
            count_and_discussion_point_relationship[count +
                                                    1] = graph_discussion_points[count][2]
            count += 1
        return count_and_discussion_point_relationship

    def build_discussion_sentiment_graph(self, graph_discussion_points):
        discussion_sentiment_graph_data = []
        columns = ['Discussion', 'Sentiment']
        discussion_sentiment_graph_data.append(columns)
        count = 0
        while count < len(graph_discussion_points):
            rows = []
            rows.append(count + 1)
            rows.append(graph_discussion_points[count])
            discussion_sentiment_graph_data.append(rows)
            count += 1
        return discussion_sentiment_graph_data

    def get_data_for_map(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        states = ['AZ', 'TX', 'GA', 'TN', 'FL', 'CA', 'DC', 'DE', 'NC', 'MS', 'VA', 'AR', 'IA', 'WA',
                  'SC', 'KY', 'WV', 'AL', 'NM', 'MT', 'NY', 'MD', 'OH', 'OK' 'PA' 'MO' 'LA' 'ID', 'IN', 'OR',
                  'MA', 'SD', 'ME', 'KS', 'UT', 'NV', 'AK']
        map_data_set = []
        columns = ['State', 'Total Monuments']
        map_data_set.append(columns)
        state_pre_text = 'US-'
        first_year = '1854'
        second_year = post_data['year']
        if second_year == '1854':
            for state in states:
                rows = []
                number_of_statues = statues_data_subset[(
                    statues_data_subset["Year Dedicated"] == 1854) & (statues_data_subset["State"] == state)]
                state = state_pre_text + state
                rows.append(state)
                rows.append(len(number_of_statues))
                if state != 'US-OKPAMOLAID':
                    map_data_set.append(rows)
        else:
            states = ['TX', 'GA', 'TN', 'FL', 'CA', 'DC', 'DE', 'NC', 'MS', 'VA', 'AR', 'IA', 'WA',
                      'SC', 'KY', 'WV', 'AL', 'NM', 'MT', 'NY', 'MD', 'OH', 'OK' 'PA' 'MO' 'LA' 'ID', 'IN', 'OR',
                      'MA', 'SD', 'ME', 'KS', 'UT', 'NV', 'AK']
            yearOne = statues_data_subset['Year Dedicated'] >= int(first_year)
            yearTwo = statues_data_subset['Year Dedicated'] <= int(second_year)
            for state in states:
                rows = []
                current_state = statues_data_subset['State'] == state
                df = statues_data_subset[(
                    current_state) & (yearOne) & (yearTwo)]
                nan_value = float("NaN")
                df.replace("", nan_value, inplace=True)
                df.dropna(subset=["Year Dedicated"], inplace=True)
                rows.append(state)
                rows.append(len(df))
                if state != 'US-OKPAMOLAID':
                    map_data_set.append(rows)
        return map_data_set

    def get_data_for_map_drilldown(self, post_data):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        # map_drill_down_data = []
        # columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        # map_drill_down_data.append(columns)
        first_year = 1854
        second_year = int(post_data['year'])
        state = post_data['state']
        state = statues_data_subset['State'] == state
        yearOne = statues_data_subset['Year Dedicated'] >= first_year
        yearTwo = statues_data_subset['Year Dedicated'] <= second_year
        map_drill_down_data = statues_data_subset[(state) & (yearOne) &
                                                          (yearTwo)]
        return
