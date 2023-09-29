import pandas as pd
import re

# Read the data from the Excel file
df = pd.read_excel('Test_Files.xlsx')

# Separate students into male and female lists
male_students = df[df['Gender'] == 'Male']
female_students = df[df['Gender'] == 'Female']

# Define a regex pattern to find names with special characters
special_characters_pattern = re.compile(r'[^\w\s]+')

# Find names with special characters
students_with_special_chars = df[df['Student Name'].str.contains(special_characters_pattern)]


import pickle

# Create or load your dataframes (e.g., male_students, female_students, students_with_special_chars)

# Save dataframes as a dictionary using Pickle
dataframes_dict = {
    'male_students': male_students,
    'female_students': female_students,
    'students_with_special_chars': students_with_special_chars
}

with open('dataframes.pkl', 'wb') as f:
    pickle.dump(dataframes_dict, f)