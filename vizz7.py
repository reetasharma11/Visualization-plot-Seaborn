import os

import matplotlib.pyplot as plt
import pandas as pd
  
#loading dataset
df= pd.read_csv(filepath_or_buffer='/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)

#creating figure
fig, axes = plt.subplots(1,1,figsize=(5,5))

axes.scatter(df['GRE Score'], df['Chance of Admit '], alpha=0.7, label='GRE Score vs Chance of Admit')
axes.scatter(df['TOEFL Score'], df['Chance of Admit '], alpha=0.7, label='TOEFL vs Chance of Admit')
#axes[1,0].scatter(df['SOP'], df['Chance of Admit '], alpha=0.7, label='SOP vs Chance of Admit')
#axes[0,0].scatter(df['GRE Score'], df['Chance of Admit '], alpha=0.7, label='GRE Score vs Chance of Admit')
axes.set_xlabel('GRE Score / TOEFL Score ')
axes.set_ylabel('chance of admit')
axes.set_title(f'Total Chance of Admit')
axes.legend()

os.makedirs('plots', exist_ok=True)
plt.savefig('plots/GRE_Chance_of_Admit_scatter.png', dpi=300)

fig, axes = plt.subplots(1,1,figsize=(5,5))

axes.scatter(df['SOP'], df['Chance of Admit '], alpha=0.7, label='SOP vs Chance of Admit')
axes.scatter(df['LOR '], df['Chance of Admit '], alpha=0.7, label='LOR vs Chance of Admit')
axes.set_xlabel('SOP / LOR ')
axes.set_ylabel('chance of admit')
axes.set_title(f'Total Chance of Admit')
axes.legend()

os.makedirs('plots', exist_ok=True)
plt.savefig('plots/SOP_LOR_Chance_of_Admit_scatter.png', dpi=300)


#plt.show()
plt.close()
