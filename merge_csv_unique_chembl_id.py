# -*- coding: utf-8 -*-
"""Merge_CSV_unique_chembl_ID.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PkxnvaejzEIRuvGcSOxyKEKl59FGdtUz
"""

import pandas as pd
from google.colab import files

# Upload CSV files to Colab
uploaded_files = files.upload()

# Load and merge CSV files
dfs = [pd.read_csv(file) for file in uploaded_files]
merged_data = pd.concat(dfs, ignore_index=True)

# Keep only one datapoint for each unique molecule_chembl_id
unique_data = merged_data.drop_duplicates(subset='molecule_chembl_id')

# Save the merged and deduplicated data to a new CSV file
unique_data.to_csv('merged_data.csv', index=False)

# Display the merged and deduplicated DataFrame
display(unique_data.head())