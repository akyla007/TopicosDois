import time
import tracemalloc

inicio = time.time()
tracemalloc.start()


def busca_sequencial_v1(x, vet):
    indice = -1
    for i in range(len(vet)):
        if vet[i] == x:
            indice = i
    return indice


def busca_sequencial_v2(x, vet):
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1


def main():
    vet = list(range(1, 10000))

    print(busca_sequencial_v1(6, vet))
    print(busca_sequencial_v2(6, vet))


if __name__ == "__main__":
    main()

fim = time.time()
tracemalloc.stop()

current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual: {current } bytes")
print(f"Pico de uso de memória: {peak } bytes")
tempo_execucao = (fim - inicio) * 1000
print(f"Tempo de execução: {tempo_execucao:.4f} milissegundos")

with open("BuscaSequencial.txt", "a") as file:
    file.write('\n')
    file.write(
        f"Tempo de execução: {tempo_execucao:.4f} milissegundos, Pico de uso de memória: {peak} bytes\n")
