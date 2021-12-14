# This file will deal with a lot of the data analysis for this project.

# importing supporting libraries
import numpy as np
import pandas as pd
import datetime

# Files that I built
from clean import *

class Data():

    def build_north_south_graph(self):
        clean = Clean()
        statues_data_subset = clean.clean_data()
        print(statues_data_subset.head())

test = Data() 
test.build_north_south_graph()

