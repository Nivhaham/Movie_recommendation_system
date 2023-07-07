import math
import os
import pandas as pd
import json

# the data looks like this:
# {"Title": "Tampa Bay Buccaneers vs. Detroit Lions", "Year": "1994", "Rated": "N/A", "Released": "13 Nov 1994", "Season": "8", "Episode": "2", "Runtime": "N/A", "Genre": "Sport", "Director": "N/A", "Writer": "N/A", "Actors": "Mike Patrick, Joe Theismann, Mark Malone, Chidi Ahanotu", "Plot": "N/A", "Language": "N/A", "Country": "N/A", "Awards": "N/A", "Poster": "N/A", "Ratings": [], "Metascore": "N/A", "imdbRating": "N/A", "imdbVotes": "N/A", "imdbID": "tt1282715", "seriesID": "tt1136193", "Type": "episode", "Response": "True"}
# I want this data:
# "Title", "Year","Released","Genre","Runtime,"Writer","Actors", "imdbID"

filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
filename_checks = os.path.dirname(os.getcwd()) + "\\Gather Data\\Movies_data.json"
relevant_cols = ["Title", "Year", "Released", "Genre", "Writer", "Actors", "Runtime", "imdbRating", "imdbID"]

print(filename_checks)
print(filename)

df = pd.read_json(filename, lines=True)
# print(df[df['Response'] == 'False'].index)
# print(df['Error'].isna() == False)

# Cleaning the json file from Errors and Responses
# Cleaning duplicates Rows (same Title)
if 'Response' in df.columns:
    df = df.drop(df[df['Response'] == 'False'].index)
if 'Error' in df.columns:
    df = df.drop(df[df['Error'].isna() == False].index)
df.drop_duplicates('Title', keep='first', inplace=True)

df = df[relevant_cols]
print(df)

df.to_json(filename, orient='records', lines=True)
