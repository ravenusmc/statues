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
        statues_data_set_by_year = statues_data_subset[(statues_data_subset['Year Dedicated'] >= yearOne) & (statues_data_subset['Year Dedicated'] <= yearTwo)]
        print(statues_data_set_by_year)


# test = Data()
# test.build_north_south_graph()
