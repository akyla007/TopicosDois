import time
import tracemalloc

inicio = time.time()
tracemalloc.start()


def busca_ternaria(vet, n, x):
    inicio = 0
    fim = n - 1

    while inicio <= fim:
        terco = (fim - inicio) // 3
        meio_esquerdo = inicio + terco
        meio_direito = inicio + 2 * terco

        if vet[meio_esquerdo] == x:
            return meio_esquerdo
        elif vet[meio_direito] == x:
            return meio_direito
        elif vet[meio_esquerdo] > x:
            fim = meio_esquerdo - 1
        elif vet[meio_direito] < x:
            inicio = meio_direito + 1
        else:
            inicio = meio_esquerdo + 1
            fim = meio_direito - 1

    return -1


vet = list(range(1, 100000000))

print(busca_ternaria(vet, len(vet)+1, 6532754))
fim = time.time()
tracemalloc.stop()

current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual: {current / 10**6} MB")
print(f"Pico de uso de memória: {peak / 10**6} MB")
tempo_execucao = (fim - inicio) * 1000
print(f"Tempo de execução: {tempo_execucao:.2f} milissegundos")

with open("BuscaTernaria.txt", "w") as file:
    file.write('\n')
    file.write(
        f"Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória: {peak / 10**6} MB\n")
