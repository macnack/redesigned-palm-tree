import time
import random
from matplotlib import pyplot as plt

# Fibonacci series

def fibonaci(len):
    a, b = 0, 1
    for _ in range(len):
        yield a
        a, b = b, a + b
    return a
    
n_values = list(range(2, 50))
execution_times = []

for n in n_values:
    start_time = time.perf_counter()
    list(fibonaci(n))
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b')
plt.title('Czas wykonania algorytmu w zależności od n')
plt.xlabel('n')
plt.ylabel('Czas wykonania (s)')
plt.grid(True)
plt.show()


# import pandas as pd
# df = pd.DataFrame({'n_values': n_values, 'execution_times': execution_times})
# df.to_csv('fibonacci.csv', index=False)
