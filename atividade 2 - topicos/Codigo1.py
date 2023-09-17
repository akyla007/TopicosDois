import tracemalloc
from random import shuffle
import time
tracemalloc.start()
inicio = time.time()


def maxVal1(A, n):
    max_val = A[0]
    for i in range(1, n):
        if A[i] > max_val:
            max_val = A[i]
    return max_val


tamanho = 10000000
lista_desordenada = list(range(1, tamanho + 1))
shuffle(lista_desordenada)

resultado = maxVal1(lista_desordenada, tamanho)
fim = time.time()
tempo_execucao = ((fim - inicio) * 1000)
current, peak = tracemalloc.get_traced_memory()
print(resultado)
print(
    f"resultado tempo: {tempo_execucao:.2f} ms, memória: {peak / (1024 * 1024)} MB")

with open("Código1.txt", "a") as file:
    file.write('\n')
    file.write(
        f"Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória:{peak / (1024 * 1024)} MB\n")
