# Created by Christine Kakalou on 14/2/2023
# Project: Healie
#

import warnings
import pandas as pd

# Example DataFrame
# Read in Excel file into a dictionary of dataframes
df_dict = pd.read_excel(r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs\EMA_ExtractedFiles\abilify\abilify.xlsx",
                        sheet_name=None)

# Concatenate all dataframes into a single dataframe
df = pd.concat(df_dict.values(), ignore_index=True)

# Remove first column
df = df.iloc[:, 1:]

# Initialize a list to hold the exploded dataframes
exploded_dfs = []

# Extract the keys of the dictionary
df_keys = df.keys().tolist()

# Split strings in each column by newline or comma character
for col in df.columns[1:]:
    df[col] = df[col].str.split(",")

df_column_length = df.shape[1]

# Iterate over the frequency columns
for i in range(1, df_column_length):
    # Extract the common and current column
    cols = [df.columns[0], df.columns[i]]
    # Explode the current column and assign the column name to a new column
    exploded_df = df.loc[:, cols].explode(df.columns[i], ignore_index=True).assign(Frequency=df.iloc[0, i][0])
    exploded_df.columns = ['SoC', 'ADE', 'Frequency']
    # Append the resulting dataframe to the list
    exploded_dfs.append(exploded_df)

# Concatenate all exploded dataframes into a single dataframe
# Concatenate all exploded dataframes into a single dataframe
df_exploded = pd.concat(exploded_dfs, axis=0, ignore_index=True)

# # Convert to JSON
json_string = df_exploded.to_json(orient='records')

# Print JSON
print(json_string)

with open(r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs\EMA_ExtractedFiles\abilify\abilify.json", 'w') as f:
    f.write(json_string)
