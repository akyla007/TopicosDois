import time
import tracemalloc

inicio = time.time()
tracemalloc.start()

def main():
    vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
    numero_procurado = 2
    posicao = -1

    for i in range(len(vet)):
        for j in range(len(vet)):
            for l in range(len(vet)):
                if vet[i] == numero_procurado and vet[j] == numero_procurado and vet[l] == numero_procurado:
                    posicao = i

    if posicao != -1:
        print("Posicao:", posicao)


if __name__ == "__main__":
    main()
    fim = time.time()
    tracemalloc.stop()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Uso de memória atual: {current } bytes")
    print(f"Pico de uso de memória: {peak } bytes")
    tempo_execucao = (fim - inicio) * 1000
    print(f"Tempo de execução: {tempo_execucao:.4f} milissegundos")

    with open("BuscaCubica.txt", "a") as file:
        file.write('\n')
        file.write(
            f"Tempo de execução: {tempo_execucao:.4f} milissegundos, Pico de uso de memória: {peak} bytes\n")
