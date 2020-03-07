#!/usr/bin/env python3


import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv', sep=',',header=0)

#df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP','LOR ' ,'CGPA','Research','Chance of Admit ']

os.makedirs('plots/seaborn_plots', exist_ok=True)

sns.set()

fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(df.corr(), annot=True, cmap='autumn')
ax.set_xticklabels(df.columns, rotation=45)
ax.set_yticklabels(df.columns, rotation=45)
plt.savefig('plots/seaborn_plots/GRE_admission_Seaborn_heatmap.png')

plt.close()

