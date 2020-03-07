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

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
# The size parameter can be either a fixed value or another columns as in here
axes.scatter(df['GRE Score'], df['TOEFL Score'], s=(df['Chance of Admit ']*100) ,
                 label=f'Chance of Admit', color='orange', marker='o',edgecolor='w', alpha=1)

#plt.clf()
#axes.scatter(df['SOP'],df['LOR '], s=(df['Chance of Admit ']*100),label=f'Chance of Admit', color='blue',marker='o',edgecolor='r',alpha=1)
#axes.set_xlabel(f'GRE')
#axes.set_ylabel(f'TOEFL')
#axes.set_title(f'GRE, TOEFL and Chance of Admit (Size)')
#axes.set_xlim([310,340])
#axes.set_ylim([105,120])
axes.legend()
plt.show()
plt.clf()
#plt.savefig(f'plots/8-matplotlib_multiple_plot_axes/multiplot_scatter_with_size.png', dpi=300)
plt.close("all")


