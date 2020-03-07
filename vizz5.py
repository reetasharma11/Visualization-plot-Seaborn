#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv', sep=',',header=0)

#df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP','LOR ' ,'CGPA','Research','Chance of Admit ']

os.makedirs('plots/seaborn_plots', exist_ok=True)

sns.set()

sorted_by_GRE_Score_df = df.sort_values('GRE Score')

sns.lineplot('GRE Score', 'TOEFL Score', data=sorted_by_GRE_Score_df)
sns.lineplot('GRE Score', 'CGPA', data=sorted_by_GRE_Score_df)
plt.legend(['GRE Score vs TOEFL Score', 'TOEFL Score vs CGPA'])
plt.savefig('plots/10-seaborn_plots/GRE_Admission_lineplot.png')
plt.clf()

sns.scatterplot('GRE Score', 'TOEFL Score', data=df)
plt.legend(['GRE Score'])
plt.savefig('plots/seaborn_plots/GRE_Admission_scatterplot.png')

