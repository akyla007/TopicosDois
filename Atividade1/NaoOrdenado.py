import random
import time
import tracemalloc

tracemalloc.start()


def main():

    gerador = random.Random()

    cont = 0
    for i in range(1005000):
        if cont < 9:
            print(f"{gerador.randint(0, 999)},", end="")
            cont += 1
        else:
            print(f"{gerador.randint(0, 999)} ")
            cont = 0


if __name__ == "__main__":

    inicio = time.time()
    main()
    fim = time.time()
    tracemalloc.stop()  # Para a medição de memória

    current, peak = tracemalloc.get_traced_memory()
    print(f"Memória utilizada: {memory_stats[0] / (1024 * 1024)} MB")
    print(f"Pico de memória: {memory_stats[1] / (1024 * 1024)} MB")
    tempo_execucao = (fim - inicio) * 1000
    print(f"Tempo de execução: {tempo_execucao:.2f} milissegundos")

    with open("NaoOrdenado.txt", "a") as file:
        file.write('\n')
        file.write(
            f"Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória: {peak / 10**6} MB\n")
