import time
from matplotlib import pyplot as plt
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n_values = list(range(2, 101))
execution_times = []
for n in n_values:
    lista = list(range(n))
    start_time = time.perf_counter()
    binary_search(lista, n)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)


# # Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b')
plt.title('Czas wykonania algorytmu w zależności od n')
plt.xlabel('n')
plt.ylabel('Czas wykonania (s)')
plt.grid(True)
# plt.show()

import pandas as pd
df = pd.DataFrame({'n_values': n_values, 'execution_times': execution_times})
df.to_csv('binary_search.csv', index=False)
