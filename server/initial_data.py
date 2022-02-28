# This file will deal with a lot of the initial data sets for this project. The file
# will essentially build the initial dataset.

# importing supporting libraries
import numpy as np
import pandas as pd
import datetime

# Files that I built
from clean import *

# Class builds the initial data set - which I will then place into the store on the client side.


class InitialData():

    def build_north_south_graph(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        first_chart_data_initial = []
        columns = ['Side', 'Count']
        first_chart_data_initial.append(columns)
        sides = ['North', 'South', 'Not Applicable']
        for side in sides:
            rows = []
            number_of_statues = len(
                statues_data_subset[(statues_data_subset.Side == side)])
            rows.append(side)
            rows.append(number_of_statues)
            first_chart_data_initial.append(rows)
        print(first_chart_data_initial)

    def see_data_types(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        print(statues_data_subset.dtypes)

    def min_value(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        pd.to_numeric(statues_data_subset['Year Dedicated'])
        print(statues_data_subset['Year Dedicated'].min())

    def min_value(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        pd.to_numeric(statues_data_subset['Year Dedicated'])
        print(statues_data_subset['Year Dedicated'].max())

    def unique_states(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        # statues_data_subset["State"].unique()
        states = ['AZ', 'TX', 'GA', 'TN', 'FL', 'CA', 'DC', 'DE', 'NC', 'MS', 'VA', 'AR', 'IA', 'WA',
                  'SC', 'KY', 'WV', 'AL', 'NM', 'MT', 'NY', 'MD', 'OH', 'OK' 'PA' 'MO' 'LA' 'ID', 'IN', 'OR',
                  'MA', 'SD', 'ME', 'KS', 'UT', 'NV', 'AK']
        states = sorted(states)
        print(states)

    def get_top_states_removed_statues(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        removed_statues = statues_data_subset['Removed After Charlottesville'] == 1
        removed_statues_data_set = statues_data_subset[(removed_statues)]
        state_counts = removed_statues_data_set['State'].value_counts().head(5)
        fourth_chart_data = []
        columns = ['State', 'Count']
        fourth_chart_data.append(columns)
        count = 0
        for state in state_counts.to_frame().index:
            rows = []
            rows.append(state)
            rows.append(int(state_counts.iloc[count]))
            fourth_chart_data.append(rows)
            count += 1
        print(fourth_chart_data)
    
    def get_top_years_statues_removed(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        # removed_statues_data_set = statues_data_subset[(removed_statues)]
        state_counts = statues_data_subset['Year Removed'].value_counts().head(15)
        print(state_counts)
        # fourth_chart_data = []
        # columns = ['State', 'Count']
        # fourth_chart_data.append(columns)
        # count = 0
        # for state in state_counts.to_frame().index:
        #     rows = []
        #     rows.append(state)
        #     rows.append(int(state_counts.iloc[count]))
        #     fourth_chart_data.append(rows)
        #     count += 1
        # print(fifth_chart_data)


test = InitialData()
test.get_top_years_statues_removed()
