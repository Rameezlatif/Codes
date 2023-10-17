#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import collections
number = collections.Counter()
with open('/media/rameez/MyDrive/Projects/QSAR_ML_Projects_Check/GSK3_Project/chembl262_chembl2850_05_bioactivity_data_2class_pIC50.csv', 'r') as input_file:
    content= input_file.read()
    print(content.count("inactive"))

