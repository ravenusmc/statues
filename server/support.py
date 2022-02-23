# This file will deal with a lot of the data analysis for this project.

# importing supporting libraries
import numpy as np
import pandas as pd
from datetime import date


class Support():

    def build_drill_down_rows(self, data):
        drilldown_data = []
        columns = ['feature_name', 'State', 'Symbol Type', 'Year Dedicated']
        drilldown_data.append(columns)
        if len(data) > 1:
            count = 0
            while count < len(data):
                rows = []
                Feature_Name = data.iat[count, 1]
                State = data.iat[count, 5]
                Symbol_type = data.iat[count, 8]
                Year_dedicated = data.iat[count, 10]
                rows.append(Feature_Name)
                rows.append(State)
                rows.append(Symbol_type)
                print(Year_dedicated)
                input()
                Year_dedicated = date(int(Year_dedicated), int(1), int(1))
                rows.append(Year_dedicated)
                drilldown_data.append(rows)
                count += 1
        else:
            rows = []
            Feature_Name = data['feature_name'].iloc[0]
            State = data['State'].iloc[0]
            Symbol_type = data['Symbol Type'].iloc[0]
            Year_dedicated = data['Year Dedicated'].iloc[0]
            rows.append(Feature_Name)
            rows.append(State)
            rows.append(Symbol_type)
            Year_dedicated = date(int(Year_dedicated), int(1), int(1))
            rows.append(Year_dedicated)
            drilldown_data.append(rows)
        return drilldown_data
