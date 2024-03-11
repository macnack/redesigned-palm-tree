import time
import random
from matplotlib import pyplot as plt

def suma_poteg(lista):
    if len(lista) < 2:
        return "Lista musi zawierać co najmniej 2 elementy."
    
    return lista[0]**2 + lista[-1]**3

# Przykład użycia
lista = [2, 3, 4, 5] # Dla tej listy wynik powinien być 2^2 + 5^3 = 4 + 125 = 129

def gen_list(n):
    return [random.randint(1, 10) for _ in range(n)]

n_values = list(range(2, 101))
execution_times = []

for n in n_values:
    lista = gen_list(n)
    start_time = time.perf_counter()
    suma_poteg(lista)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

# Rysowanie wykresu
print(sum(execution_times) / 10**9)
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b')
plt.title('Czas wykonania algorytmu w zależności od długości listy n')
plt.xlabel('Długość listy n')
plt.ylabel('Czas wykonania (s)')
plt.grid(True)
# plt.show()

import pandas as pd
df = pd.DataFrame({'n_values': n_values, 'execution_times': execution_times})
df.to_csv('suma_poteg.csv', index=False)
