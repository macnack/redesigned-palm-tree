import csv
from matplotlib import pyplot as plt

# read pandas 
import pandas as pd
df1 = pd.read_csv('suma_liczb.csv')
df2 = pd.read_csv('suma_poteg.csv')
df3 = pd.read_csv('bubble_sort.csv')
df4 = pd.read_csv('binary_search.csv')
df5 = pd.read_csv('fibonacci.csv')

# normalize
df1['execution_times'] = df1['execution_times'] / df1['execution_times'].max()
df2['execution_times'] = df2['execution_times'] / df2['execution_times'].max()
df3['execution_times'] = df3['execution_times'] / df3['execution_times'].max()
df4['execution_times'] = df4['execution_times'] / df4['execution_times'].max()
df5['execution_times'] = df5['execution_times'] / df5['execution_times'].max()

# plot
plt.figure(figsize=(10, 6))
plt.plot(df1['n_values'], df1['execution_times'], marker='o', linestyle='-', color='b', label='suma_liczb')
plt.plot(df2['n_values'], df2['execution_times'], marker='o', linestyle='-', color='r', label='suma_poteg')
plt.plot(df3['n_values'], df3['execution_times'], marker='o', linestyle='-', color='g', label='bubble_sort')
plt.plot(df4['n_values'], df4['execution_times'], marker='o', linestyle='-', color='y', label='binary_search')
plt.plot(df5['n_values'], df5['execution_times'], marker='o', linestyle='-', color='c', label='fibonacci')
plt.title('Czas wykonania algorytmu w zależności od n')
plt.xlim(0, 80)
plt.xlabel('n')
plt.ylabel('Znormalizowany czas wykonania')
plt.grid(True)
plt.legend()
plt.show()