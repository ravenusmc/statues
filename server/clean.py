# This file will clean the data

# importing supporting libraries
import numpy as np
import pandas as pd
import datetime

class Clean():

    def __init__(self):
        self.data = pd.read_csv('./data/statues.csv')
        # self.data['deadline'] = pd.to_datetime(self.data['deadline'], infer_datetime_format=True)

    def clean_data(self):
        # Seeing number of missing values 
        # print(self.data.isnull().sum())
        # See the shape of the data set 
        # print(self.data.shape)
        # Drop every row that has a missing value: 
        # statues_data_subset = self.data.dropna(how='any')
        # print(statues_data_subset.shape)
        #####
        return self.data.fillna('Not Applicable')


test = Clean()
test.clean_data()

# Video on handling missing values: 
# https://www.youtube.com/watch?v=fCMrO_VzeL8