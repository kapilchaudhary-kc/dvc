import pandas as pd
import os

#Create a sample dataframe
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,29],
    'City':['New York', 'Los Angeles', 'Chicago']
}

new_row_loc = {
    'name': 'Marco', 'Age': 45, 'City': 'Singapore'
}

df = pd.DataFrame(data)

df.loc[len(df.index)] = new_row_loc
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV File Saved at {file_path}")