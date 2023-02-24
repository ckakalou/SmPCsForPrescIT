# Created by Christine Kakalou on 20/2/2023
# Project: SmPCs for PrescIT
#

import pandas as pd
from fuzzywuzzy import fuzz
import json

SmPC_Structure = ""

# Read in Excel file into a dictionary of dataframes
df_dict = pd.read_excel(r"Data/SmPCs/EMA_ExtractedFiles/abilify/abilify.xlsx",
                        sheet_name=None)

# Concatenate all dataframes into a single dataframe
df = pd.concat(df_dict.values(), ignore_index=True)

# Remove first column
df = df.iloc[:, 1:]

# Initialize a list to hold the exploded dataframes
exploded_dfs = []

# Extract the keys of the dictionary
df_keys = df.keys().tolist()

# load soc terms
soc_terms = json.load(open(r"Data/MedDRA/SystemOrganClass.json", 'r'))
# load frequency terms
frequency_terms = json.load(open(r"Data/MedDRA/frequencies.json", 'r'))


def match_terms(df_column_list, list_terms, min_score=0):
    overall_max_score = -1
    overall_max_partial_score = -1
    overall_max_term = ''
    sum_max_score = 0
    sum_partial_score = 0

    for row in df_column_list:
        max_score = -1
        max_term = ''
        max_partial_score = -1
        for meddra_term in list_terms:
            score = fuzz.ratio(str(row), meddra_term)
            partial_score = fuzz.partial_ratio(str(row), meddra_term)
            if score > min_score and score > max_score:
                max_term = meddra_term
                max_score = score
            if partial_score > min_score:
                max_partial_score = partial_score
        sum_max_score += max_score
        sum_partial_score += max_partial_score
        if max_score > overall_max_score:
            overall_max_term = max_term
            overall_max_score = max_score
        if max_partial_score > overall_max_partial_score:
            overall_max_partial_score = max_partial_score

    mean_max_score = sum_max_score / len(df_column_list)
    partial_mean_score = sum_partial_score / len(df_column_list)

    return overall_max_term, overall_max_score, overall_max_partial_score, mean_max_score, partial_mean_score

# Check dataframe to find SoC, frequencies and ADEs columns
for columnIndex in range(len(df.columns)):
    df_column_list = df.iloc[:, columnIndex].tolist()
    soc_column_check = match_terms(df_column_list, soc_terms['terms'], min_score=80)
    if soc_column_check[1] > 90 and soc_column_check[3] > 70:
        print("SoC column found")
        df.columns.values[columnIndex] = "SoC"
    frequency_column_check = match_terms(df_column_list, frequency_terms['terms'], min_score=80)
    if frequency_column_check[2] > 90:
        if frequency_column_check[4] > 80:
            SmPC_Structure = "Horizontal"
            print("Frequency column found")
            df.columns.values[columnIndex] = "Frequency"
        else:
            SmPC_Structure = "Vertical"
            print("Specific frequency column found")
            df.columns.values[columnIndex] = frequency_column_check[0]

if SmPC_Structure == "Horizontal":
    # Extract the keys of the dictionary
    df_keys = df.keys().tolist()

    # Split strings in each column by newline character
    for col in df.columns[1:]:
        df[col] = df[col].str.split("\\n")

    # Explode ade and frequency columns
    df = df.apply(pd.Series.explode)
    df = df.reset_index(drop=True)
    df = df.iloc[1:, :]
    df.columns = ['SoC', 'Adverse Drug Event', 'Frequency']

# frequency_column_check = match_terms(df.iloc[:, 1].tolist(), frequency_terms['terms'], min_score=80)

# Find column contains ADEs - is not a SoC or frequency column
# not_in_list = ["SoC", "Frequency"]
# index = next((i for i, col in enumerate(df.columns) if col not in not_in_list), None)
# print("ADEs column index is: ", index)
# df.columns.values[index] = "Adverse Drug Event"

# Convert to JSON
json_string = df.to_json(orient='records')


with open(r"Data/SmPCs/EMA_ExtractedFiles/abilify/abilify.json", 'w') as f:
    f.write(json_string)