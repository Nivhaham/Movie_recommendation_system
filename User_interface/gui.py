"""
Main calling this python file in order to
get the user movies preference.
"""

import json
import os
import tkinter as tk
import time
data = {}


def submit_writer():
    writer_name = entry_writer.get()
    # print("Writer:", writer_name)
    return writer_name


def submit_actors():
    actors_names = entry_actors.get()
    # print("Actors:", actors_names)
    return actors_names


def get_selected_genres():
    selected_genres = [option for option, var in genre_vars.items() if var.get()]
    return selected_genres


def get_selected_movies():
    selected_movies = [option for option, var in movie_vars.items() if var.get()]
    return selected_movies


def get_data_from_user():
    data["Year"] = get_selected_movies()
    data["Genre"] = get_selected_genres()
    data["Writer"] = submit_writer()
    data["Actors"] = submit_actors()
    print(data)
    # create a file saving the user data
    filename = os.path.dirname(os.getcwd()) + "\\User_pref.jsonl"
    with open(filename, 'w') as file:
        file.write(json.dumps(data))
    return data


def exit_program():
    root.destroy()

print("Add Your Movie preferences data")
time.sleep(3)

movie_options = {
    "Very Old": False,
    "Old": False,
    "Not So Old": False,
    "Recent": False,
    "Newest": False
}

genre_options = {
    "Documentary": False,
    "Biography": False,
    "Fantasy": False,
    "Mystery": False,
    "History": False,
    "Comedy": False,
    "Animation": False,
    "Music": False,
    "Action": False,
    "Adventure": False,
    "Drama": False,
    "Romance": False,
    "Horror": False,
    "Family": False,
    "Sci-Fi": False,
    "War": False,
    "Thriller": False
}

root = tk.Tk()

# Set the window width
window_width = 500
root.geometry(f"{window_width}x400")

# Old or New Movie Label
label_movies = tk.Label(root, text="Old or New Movies?")
label_movies.pack()

# Movie Options Checkbuttons
movie_vars = {}
movie_frame = tk.Frame(root)
movie_frame.pack()

for i, (option, value) in enumerate(movie_options.items()):
    var = tk.BooleanVar(value=value)
    movie_vars[option] = var
    checkbox = tk.Checkbutton(movie_frame, text=option, variable=var)
    checkbox.grid(row=i // 5, column=i % 5, sticky="w")

# Get Selected Movies Button
button_get_movies = tk.Button(root, text="Submit", command=lambda: print(get_selected_movies()))
# button_get_movies.pack()

# Genre Label
label_genre = tk.Label(root, text="Genre")
label_genre.pack()

# Genre Options Checkbuttons
genre_vars = {}
genre_frame = tk.Frame(root)
genre_frame.pack()

for i, (option, value) in enumerate(genre_options.items()):
    var = tk.BooleanVar(value=value)
    genre_vars[option] = var
    checkbox = tk.Checkbutton(genre_frame, text=option, variable=var)
    checkbox.grid(row=i // 5, column=i % 5, sticky="w")

# Get Selected Genres Button
button_get_genres = tk.Button(root, text="Submit", command=lambda: print(get_selected_genres()))
# button_get_genres.pack()

# Writer Label, Entry, and Button
label_writer = tk.Label(root, text="Writer")
label_writer.pack()
entry_writer = tk.Entry(root)
entry_writer.pack()
button_writer = tk.Button(root, text="Submit", command=submit_writer)
# button_writer.pack()

# Actors Label, Entry, and Button
label_actors = tk.Label(root, text="Actors")
label_actors.pack()
entry_actors = tk.Entry(root)
entry_actors.pack()
button_actors = tk.Button(root, text="Submit", command=submit_actors)
# button_actors.pack()


# Exit Button
# button_exit = tk.Button(root, text="Exit", command=exit_program())
# button_exit.pack(side="bottom")

# Save Button
button_save = tk.Button(root, text="Save", command=get_data_from_user, width=10, height=3, bg="lightblue")
button_save.pack(side="bottom", anchor="se")

root.mainloop()

