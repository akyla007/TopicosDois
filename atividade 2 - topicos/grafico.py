import matplotlib.pyplot as plt

# Dados atualizados
tempos_execucao = [
    0.00, 0.00, 1.00, 16.82, 198.70, 2142.00, 24402.93, 355737.31
]  # Lista de tempos de execução em milissegundos

picos_memoria = [
    0.00033557861328125, 0.00102233876953125, 0.027843118408203125, 0.33683795837402344,
    3.426743881225586, 34.33527946472168, 343.3276882171631, 3433.2339878082275
]  # Lista de picos de uso de memória em MB

# Converter tempos de execução para segundos
tempos_execucao = [tempo / 1000 for tempo in tempos_execucao]

# Imprimindo as listas
for tempo, memoria in zip(tempos_execucao, picos_memoria):
    print(
        f"Tempo de execução: {tempo:.2f} segundos, Pico de uso de memória: {memoria:.6f} MB")

# Criar um gráfico
plt.figure(figsize=(10, 5))  # Tamanho da figura (opcional)

# Gráfico de Tempo de Execução
plt.subplot(2, 1, 1)  # 2 linhas, 1 coluna, primeiro gráfico
plt.plot(tempos_execucao, marker='o', linestyle='-', color='b', label='Dados Antigos')
plt.title('Tempo de Execução')
plt.xlabel('Amostra')
plt.ylabel('Tempo (s)')

# Gráfico de Pico de Uso de Memória
plt.subplot(2, 1, 2)  # 2 linhas, 1 coluna, segundo gráfico
plt.plot(picos_memoria, marker='o', linestyle='-', color='g', label='Dados Antigos')
plt.title('Pico de Uso de Memória')
plt.xlabel('Amostra')
plt.ylabel('Memória (MB)')

# Ajustar espaçamento entre os gráficos
plt.tight_layout()

# Salvar o gráfico como um arquivo .jpg
plt.savefig('Codigo2.jpg')

# Mostrar o gráfico
plt.show()
