
import pandas as pd
import pickle

# Load the dictionary of dataframes from the Pickle file
with open('dataframes.pkl', 'rb') as f:
    dataframes_dict = pickle.load(f)

# Access individual dataframes using keys
male_students = dataframes_dict['male_students']
female_students = dataframes_dict['female_students']
students_with_special_chars = dataframes_dict['students_with_special_chars']

# Load your dataframes (e.g., male_students, female_students, students_with_special_chars)

# Merge dataframes into one
merged_data = pd.concat([male_students, female_students, students_with_special_chars], axis=0, ignore_index=True)

merged_data.to_json('merged_data.json', orient='records')

# Shuffle the data and save it as JSON and JSONL:
# Shuffle the data
shuffled_data = merged_data.sample(frac=1)

# Save as JSON
shuffled_data.to_json('shuffled_data.json', orient='records')

# Save as JSONL (JSON Lines)
shuffled_data.to_json('shuffled_data.jsonl', orient='records', lines=True)

