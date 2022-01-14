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
        drilldown_data_graph_one = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data_graph_one .append(columns)
        yearOne = post_data['graphOneYearOne']
        yearTwo = post_data['graphOneYearTwo']
        side = post_data['side']
        statues_data_set_by_year_drill_down = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (
            statues_data_subset['Year Dedicated'] <= yearTwo) & (statues_data_subset['Side'] == side)]
        #statues_data_set_by_year_drill_down = pd.to_datetime(statues_data_set_by_year_drill_down['Year Dedicated'], format='%Y')
        if len(statues_data_set_by_year_drill_down) > 1:
            count = 0
            while count < len(statues_data_set_by_year_drill_down):
                rows = []
                Feature_Name = statues_data_set_by_year_drill_down.iat[count, 1]
                State = statues_data_set_by_year_drill_down.iat[count, 5]
                Symbol_type = statues_data_set_by_year_drill_down.iat[count, 8]
                Year_dedicated = statues_data_set_by_year_drill_down.iat[count, 10]
                rows.append(Feature_Name)
                rows.append(State)
                rows.append(Symbol_type)
                Year_dedicated = pd.to_datetime(Year_dedicated, format='%Y').year
                Year_dedicated = datetime.date(Year_dedicated, 1,1)
                # print(datetime.date(Year_dedicated))
                rows.append(Year_dedicated)
                drilldown_data_graph_one.append(rows)
                count += 1
        else:
            rows = []
            Feature_Name = statues_data_set_by_year_drill_down['feature_name'].iloc[0]
            State = statues_data_set_by_year_drill_down['State'].iloc[0]
            Symbol_type = statues_data_set_by_year_drill_down['Symbol Type'].iloc[0]
            Year_dedicated = statues_data_set_by_year_drill_down['Year Dedicated'].iloc[0]
            rows.append(Feature_Name)
            rows.append(State)
            rows.append(Symbol_type)
            rows.append(Year_dedicated)
            drilldown_data_graph_one.append(rows)
        return drilldown_data_graph_one


# test = Data()
# test.build_north_south_graph()
