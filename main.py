import os
import time
from Gather_Data import gather_Data
from Preproccess import clean_data
#from User_interface import gui
from Content_based_Filtering import suggestions

def main():
    print("Welcome To Movie Suggestion system\n")

    gather_data_response = input("Do you want to gather more data? Reply yes if so:\n")
    if gather_data_response.lower() == "yes":
        gather_Data.data_gather()
        clean_data.clean_data()
    print("\n")
    suggestions.give_a_suggestion()

if __name__ == '__main__':
    main()