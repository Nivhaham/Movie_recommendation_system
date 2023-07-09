"""
Gather Data assistant

Some function that are used
to connect to the api, get the data,
write the data to a file as jsonl.
"""

import json
import random
import requests
import os


def write_json_line_by_line(filename, data):
    """

    :param filename: The filename that is written to.
    :param data:The written data
    :return: Void
    """
    with open(filename, "w") as my_data:
        for item in data:
            my_data.write(json.dumps(item))
            my_data.write("\n")


def append_movies_to_db(filename, data):
    """
    appending current data with previous data

    :param filename: The filename that is written to.
    :param data:The written data
    :return: Void
    """
    print(os.path.dirname(filename))
    # print(filename)
    try:
        with open(filename, "r") as file:
            existing_data = []
            for line in file:
                try:
                    json_data = json.loads(line)
                    existing_data.append(json_data)
                except json.JSONDecodeError:
                    pass
    except FileNotFoundError:
        existing_data = []

    # Append new data to the existing data
    for d in data:
        existing_data.append(d)

    # Write the updated data back to the file
    write_json_line_by_line(filename, existing_data)


def get_random_300_movies(api_key):
    """
    :param api_key: The api key
    :return: A list of all gathered data
    """
    THREE_HUNDRED = 300
    data = []
    for i in range(THREE_HUNDRED):
        movie_id = random.randint(0, 85000)
        id = "tt" + "12" + str(movie_id)
        r = requests.get(f"http://www.omdbapi.com/?i={id}&apikey={api_key}")
        data.append(json.loads(r.text))
    print(data)
    return data
