import matplotlib.pyplot as plt

# Dados atualizados
tempos_execucao = [12.3123 * 60 * 1000, 1471111.21220, 3781.23720]  # Tempo de execução em milissegundos
picos_memoria = [63000.00, 65560.00, 84496.00]  # Pico de uso de memória em bytes

# Criar um gráfico
plt.figure(figsize=(10, 5))  # Tamanho da figura (opcional)

# Gráfico de Tempo de Execução
plt.subplot(2, 1, 1)  # 2 linhas, 1 coluna, primeiro gráfico
plt.plot(tempos_execucao, marker='o', linestyle='-', color='b')
plt.title('Tempo de Execução')
plt.xlabel('Amostra')
plt.ylabel('Tempo (ms)')

# Gráfico de Pico de Uso de Memória
plt.subplot(2, 1, 2)  # 2 linhas, 1 coluna, segundo gráfico
plt.plot(picos_memoria, marker='o', linestyle='-', color='g')
plt.title('Pico de Uso de Memória')
plt.xlabel('Amostra')
plt.ylabel('Memória (bytes)')

# Ajustar espaçamento entre os gráficos
plt.tight_layout()

# Salvar o gráfico como um arquivo .jpg
plt.savefig('BuscaCubica.jpg')

# Mostrar o gráfico
plt.show()
