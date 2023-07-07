import os
import pandas as pd
import json
import re
import numpy as np

'''idea, for ranges of years +1, for specific genre +3, for writer +7, for actors +3'''
filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
user_pref_file = os.path.dirname(os.getcwd()) + "\\User_pref.jsonl"

df = pd.read_json(filename, lines=True)
df_user_pref = pd.read_json(user_pref_file, lines=True)

print(df_user_pref["Year"])
for year in df_user_pref["Year"]:
    print(year)

for row in df.iterrows():
    print(row)
    print(row['Year'])
    #if row["Year"] == 2008:
    #    print(row)

def calculate_score():
    total_score = 0

    def calculate_year_logic():

        if int(df['Year']) > 2000 and 'Recent' in df_user_pref["Year"]:
            pass
    #        total_score+=1

print(df_user_pref)
# print(df.columns)
# print(df['Runtime'].unique())
# print(df['Genre'].unique())
