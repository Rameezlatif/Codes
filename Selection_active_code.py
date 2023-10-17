# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



df = pd.read_csv('IRAK4_05_bioactivity_data_2class_pIC50.csv')

# Remove inactive (code to remove inactive compounds)
df_2= df[df['class'] != 'inactive']

# Save the  file into CSV

df_final=df_2.to_csv ('IRAK4_06_bioactivity_QSAR.csv')

