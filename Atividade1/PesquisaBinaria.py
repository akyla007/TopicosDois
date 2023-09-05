import tracemalloc
import time

def pesquisa_binaria(x, v, e, d):
    meio = (e + d) // 2
    if v[meio] == x:
        return meio
    if e >= d:
        return -1
    elif v[meio] < x:
        return pesquisa_binaria(x, v, meio + 1, d)
    else:
        return pesquisa_binaria(x, v, e, meio - 1)

if __name__ == "__main__":
    tracemalloc.start()  # Inicia a medição de memória
    vet = list(range(1, 1000000))
    inicio = time.time()  # Início da medição de tempo
    resultado = pesquisa_binaria(692, vet, 0, 10000)
    print("Resultado:", resultado)
    fim = time.time()  # Fim da medição de tempo

    # Mede a quantidade de memória usada
    current, peak = tracemalloc.get_traced_memory()
    print(f"Uso de memória atual: {current / 10**6} MB")
    print(f"Pico de uso de memória: {peak / 10**6} MB")
    tempo_execucao = (fim - inicio) * 1000
    print(f"Tempo de execução: {tempo_execucao:.2f} milissegundos")

    tracemalloc.stop()  # Para a medição de memória
    with open("PesquisaBinaria.txt", "a") as file:
        file.write('\n')
        file.write(f"Tempo de execução: {tempo_execucao:.2f} milissegundos, Pico de uso de memória: {peak / 10**6} MB\n")
