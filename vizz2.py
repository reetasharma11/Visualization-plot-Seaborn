import os

import matplotlib.pyplot as plt
import pandas as pd

#loading dataset
df= pd.read_csv(filepath_or_buffer='/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)

#creating figure
fig, axes = plt.subplots(2,2,figsize=(8,8))

axes[0,0].scatter(df['GRE Score'],df['CGPA'])
axes[0,0].set_title('Gre va Cgpa')
axes[0,0].set_xlabel(f'GRE')
axes[0,0].set_ylabel(f'CGPA')

axes[0,1].scatter(df['TOEFL Score'],df['CGPA'])
axes[0,1].set_title('TOEFL va Cgpa')
axes[0,1].set_xlabel(f'TOEFL Score')
axes[0,1].set_ylabel(f'CGPA')

axes[1,0].scatter(df['GRE Score'],df['Chance of Admit '])
axes[1,0].set_title('Gre va Chance of Admit')
axes[1,0].set_xlabel(f'GRE')
axes[1,0].set_ylabel(f'Chance of Admit')

axes[1,1].scatter(df['TOEFL Score'],df['Chance of Admit '])
axes[1,1].set_title('TOEFL va Chance of Admit')
axes[1,1].set_xlabel(f'TOEFL')
axes[1,1].set_ylabel(f'Chance of Admit')
plt.tight_layout()
os.makedirs('plots', exist_ok=True)

plt.savefig('plots/multiple_plot_figure.png', dpi=300)
#p#lt.savefig('plots/multiple_plot_figure/plot.svg', dpi=300)
#pl#t.savefig('plots/multiple_plot_figure/plot.pdf', dpi=300)

plt.close()

