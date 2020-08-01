import pandas as pd
import os
import json
from functools import reduce



path1 = 'C:/Users/Owner/GitHub/spider-projects/forfun/homefinder_data.json'
path2 = 'C:/Users/Owner/GitHub/spider-projects/forfun/realtor_data.json'
path3 = 'C:/Users/Owner/GitHub/spider-projects/forfun/homes_data.json'

homefinder_df = pd.read_json(path1)
realtor_df = pd.read_json(path2)
homes_df = pd.read_json(path3)

dataframes = [homefinder_df, realtor_df, homes_df]

# dfs = {0: homefinder_df, 1: realtor_df, 2: homes_df}
# suffix = ("_homefinder", "_realtor", "_homes")
# for i in dfs:
#     dfs[i] = dfs[i].add_suffix(suffix[i])



df = reduce(lambda  left,right: pd.merge(left, right, on=["address", "city", "state", "zipcode"],
                                            how='outer'), dataframes)


df.to_csv('C:/Users/Owner/GitHub/spider-projects/forfun/master_list.csv')








