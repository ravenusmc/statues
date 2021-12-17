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
        sides = ['North', 'South']
        for side in sides: 
            number_of_statues = len(statues_data_subset[(statues_data_subset.Side == side)])
            print(number_of_statues)


test = InitialData()
test.build_north_south_graph()
