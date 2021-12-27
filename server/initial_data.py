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
        Year Dedicated                   object


test = InitialData()
test.see_data_types()

