"""
Preprocess

run when you want to clean bad rows from the database.
"""

import math
import os
import pandas as pd
import json
import re


def clean_data(filename=os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"):
    """

    :param filename: the file were the data is stored
    :return: removing bad rows from dataset
    """
    # filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
    filename_checks = os.path.dirname(os.getcwd()) + "\\Gather_Data\\Movies_data.json"
    relevant_cols = ["Title", "Year", "Released", "Genre", "Writer", "Actors", "Runtime", "imdbRating", "imdbID"]

    print(filename_checks)
    print(filename)

    df = pd.read_json(filename, lines=True)
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


# filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
#filename_from_main = os.getcwd() + "\\Movies_data.jsonl"

#clean_data(filename_from_main)
