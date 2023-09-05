import time
import tracemalloc

inicio = time.time()
tracemalloc.start()


def main():
    vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
    numero_procurado = 9
    contador = 0
    posicao = -1
    entrou = False

    for i in range(len(vet)):
        for j in range(i, len(vet)):
            if vet[i] == numero_procurado:
                if not entrou:
                    posicao = i
                    if vet[j] == numero_procurado:
                        contador += 1
                entrou = True

    if entrou:
        print("Posicao:", posicao, "- contador de repeticao:", contador)

if __name__ == "__main__":
    main()
fim = time.time()
tracemalloc.stop()

current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual: {current } bytes")
print(f"Pico de uso de memória: {peak } bytes")
tempo_execucao = (fim - inicio) * 1000
print(f"Tempo de execução: {tempo_execucao:.4f} milissegundos")

with open("BuscaQuadratica.txt", "a") as file:
    file.write('\n')
    file.write(
        f"Tempo de execução: {tempo_execucao:.4f} milissegundos, Pico de uso de memória: {peak} bytes\n")
