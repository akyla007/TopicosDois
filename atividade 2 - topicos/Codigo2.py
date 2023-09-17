import tracemalloc
from random import shuffle
import time
tracemalloc.start()
inicio = time.time()


def maxVal2(A, init, end):
    if end - init <= 1:
        return max(A[init], A[end])
    else:
        m = (init + end) // 2
        v1 = maxVal2(A, init, m)
        v2 = maxVal2(A, m + 1, end)
        return max(v1, v2)


tamanho = 100000000
lista_desordenada = list(range(1, tamanho + 1))
shuffle(lista_desordenada)

resultado = maxVal2(lista_desordenada, 0, tamanho - 1)  # Correção nos índices
fim = time.time()
tempo_execucao = ((fim - inicio) * 1000)
current, peak = tracemalloc.get_traced_memory()
print(resultado)
print(
    f"Resultado: {resultado}, Tempo de execução: {tempo_execucao:.2f} ms, Pico de uso de memória: {peak / (1024 * 1024)} MB")

with open("Código2.txt", "a") as file:
    file.write(
        f" Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória: {peak / (1024 * 1024)} MB\n")
    file.write('\n')
