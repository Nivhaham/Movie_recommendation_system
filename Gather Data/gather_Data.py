# OMDB - open movie database
import json
import requests
import os
import useful_functions



def data_gather():
    """
    The function connect to the omdb api, takes 300 rows
    of data from it and adding it to a jsonl file called
    Movies_data.jsonl
    the site address is: https://www.omdbapi.com/
    the id for movies are in specific format ranging tt1282000 - tt12ddddd
    :return:
    """
    my_api_key = "14cca8a7"

    filename_for_checks = os.getcwd() +"\\Movies_data.json"
    filename = os.path.dirname(os.getcwd()) + "\\Movies_data.jsonl"
    # r = requests.get(f"http://www.omdbapi.com/?i=tt1283001&apikey={my_api_key}")
    # data = json.loads(r.text)

    data = useful_functions.get_random_300_movies(my_api_key)
    useful_functions.append_movies_to_db(filename, data)

data_gather()