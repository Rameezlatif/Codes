# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("/media/rameez/MyDrive/Projects/QSAR_ML_Projects_Check/NLRP3_Machine_Learning/descriptor_list.csv")


# dropping ALL duplicate values
data = data.loc[:,~data.T.duplicated(keep='last')]


# displaying data

data.to_csv('descriptor_list_new.csv', index=False)
