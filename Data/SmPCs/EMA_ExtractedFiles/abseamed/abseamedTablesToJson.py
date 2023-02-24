# Created by Christine Kakalou on 14/2/2023
# Project: Healie
#

import warnings
import pandas as pd

# Example DataFrame
# Read in Excel file into a dictionary of dataframes
df_dict = pd.read_excel(r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs\EMA_ExtractedFiles\abseamed\abseamed.xlsx",
                        sheet_name=None)

# Concatenate all dataframes into a single dataframe
df = pd.concat(df_dict.values(), ignore_index=True)

# Remove first column
df = df.iloc[:, 1:]

# Initialize a list to hold the exploded dataframes
exploded_dfs = []

# Extract the keys of the dictionary
df_keys = df.keys().tolist()

# Split strings in each column by newline character
for col in df.columns[1:]:
    df[col] = df[col].str.split(",")

# Explode ade and frequency columns
df = df.apply(pd.Series.explode)
df = df.reset_index(drop=True)
df =  df.iloc[1:, :]
df.columns = ['SoC', 'ADE', 'Frequency']

# Convert to JSON
json_string = df.to_json(orient='records')

with open(r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs\EMA_ExtractedFiles\abseamed\abseamed.json", 'w') as f:
    f.write(json_string)
