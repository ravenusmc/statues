# This file will deal with a lot of the data analysis for this project.

# importing supporting libraries
import numpy as np
import pandas as pd
import datetime

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


# test = Data()
# test.build_north_south_graph()
