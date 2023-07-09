"""

Run this in order to get a suggestion from the system.

"""

import os
import pandas as pd
import json
import re
import numpy as np

filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
user_pref_file = os.path.dirname(os.getcwd()) + "\\User_pref.jsonl"

df = pd.read_json(filename, lines=True)
df_user_pref = pd.read_json(user_pref_file, lines=True)
score_list = [0 for _ in range(df.shape[0] + 1)]  # this score each movie in the dataset in correlation to user input.


# This work but its bad implementation because don't abuse pandas func.

def score_Actor():
    # Scoring by Actor
    for row_index, movie_Actors in enumerate(df["Actors"]):
        movie_Actors = movie_Actors.split(',')
        for movie_Actor in movie_Actors:
            movie_Actor = movie_Actor.lstrip()
            for actors in df_user_pref["Actors"]:
                actors = actors.split(',')
                for actor in actors:
                    actor = actor.lstrip()
                    if actor == movie_Actor:
                        score_list[row_index + 1] += 3
                        break


def score_Writer():
    # Scoring by Writer
    for row_index, movie_Writers in enumerate(df["Writer"]):
        movie_Writers = movie_Writers.split(',')
        for movie_Writer in movie_Writers:
            movie_Writer = movie_Writer.lstrip()
            for writers in df_user_pref["Writer"]:
                writers = writers.split(',')
                for writer in writers:
                    writer = writer.lstrip()
                    if writer in movie_Writer:
                        score_list[row_index + 1] += 6
                        #print(row_index, movie_Writers)
                        break


def score_Genre():
    # Scoring by Genre
    for row_index, movie_genres in enumerate(df["Genre"]):
        movie_genres = movie_genres.split(',')
        # print(row_index,movie_genre)
        for movie_genre in movie_genres:
            movie_genre = movie_genre.lstrip()
            for geners in df_user_pref["Genre"]:
                for genre in geners:
                    genre = genre.lstrip()
                    if genre == movie_genre:
                        score_list[row_index + 1] += 3
                        #print(row_index + 1, movie_genre)
                        break
    #print(score_list)


def score_Year():
    # Scoring by years
    for row_index, movie_year in enumerate(df["Year"]):
        for years in df_user_pref["Year"]:
            for year in years:
                if year == "Very Old" and movie_year < "1970":
                    score_list[row_index + 1] += 1
                elif year == "Old" and "1985" > movie_year > "1970":
                    score_list[row_index + 1] += 1

                elif year == "Not So Old" and "2000" > movie_year > "1985":
                    score_list[row_index + 1] += 1

                elif year == "Recent" and "2010" > movie_year > "2000":
                    score_list[row_index + 1] += 1

                elif year == "Newest" and movie_year > "2010":
                    score_list[row_index + 1] += 1

    #print(score_list)


filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
user_pref_file = os.path.dirname(os.getcwd()) + "\\User_pref.jsonl"


def give_a_suggestion():
    """
    The function calculate which movies are the most fit
    compare to what the user has entered.
    :return: Names of movies suggested by the system.
    """
    score_Year()
    score_Actor()
    score_Genre()
    score_Writer()
    #i =input("How many suggestion do you want?")
    top_suggestions_indexes = sorted(range(len(score_list)), key=lambda i: score_list[i], reverse=True)[:5]
    #print(top_suggestions_indexes)
    print("The System offer those movies:\n ")
    for suggested_movie_index in top_suggestions_indexes:
        print(df.iloc[suggested_movie_index]["Title"],end=", ")
    print("\n\nEnjoy!")

give_a_suggestion()
