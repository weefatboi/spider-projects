import pandas as pd
import os
import json



path1 = 'C:/Users/Owner/GitHub/spider-projects/forfun/homefinder_data.json'
path2 = 'C:/Users/Owner/GitHub/spider-projects/forfun/realtor_data.json'

homefinder_df = pd.read_json(path1)
realtor_df = pd.read_json(path2)

df = pd.merge(homefinder_df, realtor_df,
            how="outer",
            on=["address", "city", "state", "zipcode"],
            suffixes=("_homefinder", "_realtor"))

df.to_csv('C:/Users/Owner/GitHub/spider-projects/forfun/master_list.csv')








