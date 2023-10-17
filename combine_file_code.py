import os
import pandas as pd

master_df= pd.DataFrame()

for file in os.listdir(os.getcwd()):
	if file.endswith('.csv'):
		master_df= master_df.append(pd.read_csv(file))


master_df.to_csv('bioactivity_curated_chembl262_chembl2095188.csv', index=False)
