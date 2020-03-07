#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


df = pd.read_csv(filepath_or_buffer='/home/reeta/Python-Visualization/graduate_admissions/Admission_Predict.csv',
                      sep=',',
                      header=0)

#pretty_print("Admission dataframe", admsn.to_string())
#pretty_print("Admission columns", admsn.columns)




os.makedirs('plots/GRE_dataset_exploration', exist_ok=True)

# Another useful dataset exploration technique involves comparing multiple columns of the dataset
# The enumerate functions will generate pairs of indexes elements
for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            print(f'Generating {column1} to {column2} plot')
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/GRE_dataset_exploration/Admission_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
