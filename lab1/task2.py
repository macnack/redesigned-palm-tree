# Zaimplementuj funkcję obliczającą sumę liczb naturalnych od 0 do n. Zbadaj złożoność obliczeniową algorytmu poprzez przygotowanie wykresu czasu wykonania algorytmu w zależności od n, do pomiaru czasu wykorzystaj perf_counter z biblioteki time. Wykonaj eksperymenty dla n od 2 do 50. Porównaj wyniki z teorią.

import time
import random
from matplotlib import pyplot as plt

def suma_liczb(n):
    return sum(range(n+1))

n_values = list(range(2, 101))
execution_times = []

for n in n_values:
    start_time = time.perf_counter_ns()
    suma_liczb(n)
    end_time = time.perf_counter_ns()
    execution_times.append(end_time - start_time)

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b')
plt.title('Czas wykonania algorytmu w zależności od n')
plt.xlabel('n')
plt.ylabel('Czas wykonania (ns)')
plt.grid(True)
# plt.show()

import pandas as pd
df = pd.DataFrame({'n_values': n_values, 'execution_times': execution_times})
df.to_csv('suma_liczb.csv', index=False)
