import random
import time
import tracemalloc


def main():
    gerador = random.Random()

    cont = 0
    for i in range(10005000):
        if cont < 9:
            print(f"{i + gerador.randint(0, 1)},", end="")
            cont += 1
        else:
            print(f"{i + gerador.randint(0, 1)} ")
            cont = 0


if __name__ == "__main__":
    tracemalloc.start()
    inicio = time.time()
    main()
    fim = time.time()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Uso de memória atual: {current / 10**6} MB")
    print(f"Pico de uso de memória: {peak / 10**6} MB")
    tempo_execucao = (fim - inicio) * 1000
    print(f"Tempo de execução: {tempo_execucao:.2f} milissegundos")

    tracemalloc.stop()  # Para a medição de memória
    with open("Ordenado.txt", "a") as file:
        file.write('\n')
        file.write(
            f"Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória: {peak / 10**6} MB\n")
