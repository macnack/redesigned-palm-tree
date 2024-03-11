import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def gen_list(n):
    return [random.randint(1, 10) for _ in range(n)]

n_values = list(range(2, 50))
execution_times = []
for n in n_values:
    lista = gen_list(n)
    start_time = time.perf_counter()
    bubble_sort(lista)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

# # Rysowanie wykresu
import matplotlib.pyplot as plt
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b')
plt.title('Czas wykonania algorytmu w zależności od n')
plt.xlabel('n')
plt.ylabel('Czas wykonania (s)')
plt.grid(True)
plt.show()

import pandas as pd
df = pd.DataFrame({'n_values': n_values, 'execution_times': execution_times})
df.to_csv('bubble_sort.csv', index=False)