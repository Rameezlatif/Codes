import pandas as pd
data = pd.read_csv('/media/rameez/MyDrive/Projects/GSK3 Project/Bioactivity app/Copy_descriptor/descriptors_output.csv')
#data.drop_duplicates()

#data2

#data2.to_csv('descriptor_list.csv', index=False)


df2 = data.T.drop_duplicates().T

df2.to_csv('descriptor_list.csv' , index=False)

#df2 = data.T.groupby(level=0).first().T

#df2.to_csv('descriptor_list.csv', index= False)

