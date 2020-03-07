import os

import matplotlib.pyplot as plt
import pandas as pd

#loading dataset
df= pd.read_csv(filepath_or_buffer='/home/reeta/python-notebook/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)
#creating figure
#os.makedirs('plots/8-matplotlib_multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(2,2, figsize=(8, 8))





axes[0,0].scatter(df['SOP'],df['LOR '], s=(df['University Rating']*100),label=f'university rating', color='blue',marker='o',edgecolor='r',alpha=1)
axes[0,0].set_title('SOP vs LOR w.r.t university rating')
axes[0,0].set_xlabel(f'SOP')
axes[0,0].set_ylabel(f'LOR')

axes[0,1].scatter(df['GRE Score'],df['TOEFL Score'], s=(10*df['Chance of Admit '])**2.5,label=f'Chance of Admit', color='orange',marker='o',edgecolor='r',alpha=1)

axes[0,1].set_title('GRE vs TOEFL w.r.t Chance of Admit')
axes[0,1].set_xlabel(f'GRE')
axes[0,1].set_ylabel(f'TOEFL')

axes[1,0].scatter(df['GRE Score'],df['CGPA'], s=(10*df['Chance of Admit '])**2.5,label=f'Chance of Admit', color='orange',marker='o',edgecolor='r',alpha=1)
axes[1,0].set_title('GRE vs CGPA w.r.t Chance of Admit')
axes[1,0].set_xlabel(f'GRE')
axes[1,0].set_ylabel(f'CGPA')

axes[1,1].scatter(df['TOEFL Score'],df['CGPA'], s=(10*df['Chance of Admit '])**2.5,label=f'Chance of Admit', color='orange',marker='o',edgecolor='r',alpha=1)
axes[1,1].set_title('TOEFL va CGPA')
axes[1,1].set_xlabel(f'TOEFL')
axes[1,1].set_ylabel(f'CGPA')
#axes[1,1].legend()
plt.tight_layout()
os.makedirs('plots', exist_ok=True)

#plt.show()
plt.savefig('plots/multiple_axes_figure_plot.png', dpi=300)
plt.close()
