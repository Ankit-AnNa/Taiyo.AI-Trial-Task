# -*- coding: utf-8 -*-
"""Taiyo.AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GyTUTDfW1xqeDY1_Gj58NSMECAyGIpe0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("WS_LBS_D_PUB_csv_col.csv")
df.shape

df.head(5)

df = df.drop(index=1)
df.head

df = df.reset_index(drop=True)
df.head(5)

df.info()

df = df.copy()

df.isna().sum()

for label, content in df.items():
    if pd.api.types.is_string_dtype(content):
        print(label)

for label, content in df.items():
    if pd.api.types.is_string_dtype(content):
        df[label] = content.astype("category").cat.as_ordered()

df.info()

df.isnull().sum()/len(df)

for label, content in df.items():
    if pd.api.types.is_numeric_dtype(content):
        print(label)

for label, content in df.items():
    if pd.api.types.is_numeric_dtype(content):
        if pd.isnull(content).sum():
            print(label)

df.isna().sum()

# Check for columns which aren't numeric
for label, content in df.items():
    if not pd.api.types.is_numeric_dtype(content):
        print(label)

df.head(5)

len(df)

df.describe()

dataset = pd.read_csv('WS_LBS_D_PUB_csv_col.csv', header=0, index_col=0)
values = dataset.values
#specify columns to plot
grps = [0, 1, 2, 3, 4, 5, 6]
i = 1
#Plotting each item
plt.figure(figsize=([15, 15]))
for group in grps:
    plt.subplot(len(grps), 1, i)
    plt.plot(values[:, group])
    plt.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
plt.show()

df.corr()

# Let's make our correlation matrix a little prettier
corr_matrix = df.corr()
fig, ax = plt.subplots(figsize=(40, 40))
ax = sns.heatmap(corr_matrix,
                 annot=True,
                 linewidths=0.5,
                 fmt=".2f",
                 cmap="YlGnBu");
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

"""**Note:** I've only fitted model on a small subset to save time I can always increase the dataset on train to increase its accuracy and score of other evaluation metrics."""

