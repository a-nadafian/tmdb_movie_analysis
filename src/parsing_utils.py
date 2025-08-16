import ast
import numpy as np


# Define a function to extract the 'name' from each dictionary in a list
def extract_names(data_list):
    names = []
    for item in data_list:
        names.append(item['name'])
    return names


# Define a function to find the director in the crew list
def get_director(crew_list):
    # Loop through each member in the crew list
    for member in crew_list:
        # Check if the member's job is 'Director'
        if member['job'] == 'Director':
            # If it is, return their name
            return member['name']
    # If no director is found after checking everyone, return NaN (Not a Number)
    return np.nan


# Ensure the 'genres' column is converted from string to list
# We add a check to handle potential empty or malformed data
def safe_literal_eval(s):
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        return []  # Return an empty list if there's an error
