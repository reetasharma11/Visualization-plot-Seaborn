#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv', sep=',',header=0)

#df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP','LOR ' ,'CGPA','Research','Chance of Admit ']

# We remove the id column as it's useless for any data exploration
#df.drop('Serial No.', axis=1, inplace=True)

os.makedirs('plots', exist_ok=True)

# All the plots in this section use the breast cancer dataset as base

# Example of creating a Histogram plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.hist(df['GRE Score'], bins=15, color='g', label='GRE Score')
axes.set_title('GRE Score')
axes.set_xlabel('GRE Score')
#axes.set_ylabel('no. of people')
axes.legend()
plt.savefig('plots/GRE_Score_hist.png', dpi=300)
#
# Example of creating a Pie plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.pie(df['Research'].value_counts(), labels=df['Research'].value_counts().index.tolist(), autopct='%1.1f%%')
axes.set_title('Research')
axes.legend()
plt.savefig('plots/research.png', dpi=300)

# Example of creating a Bar plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.bar(np.arange(0, len(df['Chance of Admit '])), df['Chance of Admit '], color='y', label='Chance of Admit ')
axes.set_title('Chances of admit')
axes.set_xlabel('Index')
axes.set_ylabel('Chance of admit')
axes.legend()
plt.savefig('plots/Admission_bar_plot.png', dpi=300)

## Example of creating a Correlation Heatmap plot
fig, axes = plt.subplots(1, 1, figsize=(20, 20))
#df['encoded_Chance of Admit']=df['Chance of Admit '].map({0:1})
correlation = df.corr().round(2)
im = axes.imshow(correlation)
cbar = axes.figure.colorbar(im, ax=axes)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
numrows = len(correlation.iloc[0])
numcolumns = len(correlation.columns)
axes.set_xticks(np.arange(numrows))
axes.set_yticks(np.arange(numcolumns))
axes.set_xticklabels(correlation.columns)
axes.set_yticklabels(correlation.columns)
plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(numrows):
    for j in range(numcolumns):
        text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
axes.set_title('Heatmap of Correlation of Dimensions')
fig.tight_layout()
plt.savefig('plots/Admit_correlation_heatmap.png')




#Creating 3D plots                                                              
gre = df#df[df['GRE Score'] == 'G']
toefl = df#df[df['TOEFL Score'] == 'T']
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection = '3d')

line1=axes.scatter(gre['LOR '], gre['SOP'], gre['University Rating'])
line2=axes.scatter(toefl['LOR '], toefl['SOP'], toefl['University Rating'])

axes.legend((line1, line2), ('gre', 'toefl'))
axes.set_xlabel('LOR')
axes.set_ylabel('SOP')
axes.set_zlabel('University Rating')
plt.savefig('plots/Admit_scatter_3d.png')
#plt.show()
plt.close()

