import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import time

class SmartFitSimulator:
    def __init__(self, halteres, total_organizados, total_desorganizados):
        self.halteres = halteres  # Quantidade de halteres em pares
        self.total_organizados = total_organizados  # Total de pessoas organizadas
        self.total_desorganizados = total_desorganizados  # Total de pessoas desorganizadas
        self.suporte = self.inicializa_suporte()

    def inicializa_suporte(self):
        """
        Inicializa o suporte com os halteres nas posições corretas.
        """
        suporte = {}
        for peso, quantidade in self.halteres.items():
            suporte[peso] = [peso] * quantidade
        return suporte

    def simula_dia(self):
        """
        Simula um dia de movimentação na seção de Peso Livre.
        """
        # Simula ações dos organizados
        for _ in range(self.total_organizados):
            self.acao_organizado()

        # Simula ações dos desorganizados
        for _ in range(self.total_desorganizados):
            self.acao_desorganizado()

        return self.calcula_desordem()

    def acao_organizado(self):
        """
        Representa a ação de uma pessoa organizada: pega um haltere e o devolve ao local correto.
        """
        peso = self.escolhe_peso()
        if self.suporte[peso]:
            self.suporte[peso].pop()
        if len(self.suporte[peso]) < self.halteres[peso]:
            self.suporte[peso].append(peso)
        else:
            self.devolve_em_lugar_aleatorio(peso)

    def acao_desorganizado(self):
        """
        Representa a ação de uma pessoa desorganizada: pega um haltere e o devolve em qualquer lugar.
        """
        peso = self.escolhe_peso()
        if self.suporte[peso]:
            self.suporte[peso].pop()
        self.devolve_em_lugar_aleatorio(peso)

    def escolhe_peso(self):
        """
        Escolhe aleatoriamente um peso disponível para ser usado.
        """
        pesos_disponiveis = [peso for peso, halteres in self.suporte.items() if halteres]
        return random.choice(pesos_disponiveis)

    def devolve_em_lugar_aleatorio(self, peso):
        """
        Devolve um haltere em um lugar aleatório.
        """
        pesos_possiveis = list(self.suporte.keys())
        local_aleatorio = random.choice(pesos_possiveis)
        self.suporte[local_aleatorio].append(peso)

    def calcula_desordem(self):
        """
        Calcula o nível de desordem no suporte.
        """
        total_desorganizados = 0
        for peso, halteres in self.suporte.items():
            total_desorganizados += sum(1 for h in halteres if h != peso)
        return total_desorganizados

    def executa_simulacoes(self, num_simulacoes):
        """
        Executa múltiplas simulações para calcular a média de desordem.
        """
        resultados = [self.simula_dia() for _ in range(num_simulacoes)]
        media_desordem = np.mean(resultados)
        desvio_padrao = np.std(resultados)

        if num_simulacoes > 1 and desvio_padrao > 0:
            intervalo_confianca = norm.interval(0.95, loc=media_desordem, scale=desvio_padrao / np.sqrt(num_simulacoes))
        else:
            intervalo_confianca = (media_desordem, media_desordem)

        return resultados, media_desordem, desvio_padrao, intervalo_confianca

def plot_histograma(resultados):
    """
    Plota a distribuição dos resultados das simulações.
    """
    plt.hist(resultados, bins=20, edgecolor='black', alpha=0.7)
    plt.title('Distribuição da Desordem ao Final do Dia')
    plt.xlabel('Unidades Desorganizadas')
    plt.ylabel('Frequência')
    plt.show()  # Bloqueante para evitar fechamento automático

def plot_impacto_porcentagem(halteres, total_pessoas, num_simulacoes):
    """
    Analisa o impacto da porcentagem de desorganizados na desordem média.
    """
    porcentagens = np.arange(0.0, 1.1, 0.1)
    medias = []
    for perc in porcentagens:
        total_organizados = int(total_pessoas * (1 - perc))
        total_desorganizados = int(total_pessoas * perc)
        simulador = SmartFitSimulator(halteres, total_organizados, total_desorganizados)
        _, media, _, _ = simulador.executa_simulacoes(num_simulacoes)
        medias.append(media)

    plt.plot(porcentagens * 100, medias, marker='o')
    plt.title('Impacto da Proporção de Desorganizados')
    plt.xlabel('Porcentagem de Desorganizados (%)')
    plt.ylabel('Média de Desordem')
    plt.grid()
    plt.show()  # Bloqueante para evitar fechamento automático

# Configurações
halteres_padrao = {
    10: 2, 12: 2, 14: 2, 16: 3, 18: 6,
    20: 5, 22: 5, 24: 5, 26: 5, 28: 5,
    30: 5, 32: 4, 34: 4, 36: 2
}

# Entrada do usuário
print("Bem-vindo ao Simulador de Desordem da Academia!")
try:
    num_simulacoes = int(input("Digite o número de simulações: "))
    total_pessoas = int(input("Digite o número total de frequentadores: "))
    total_desorganizados = int(input("Digite o número de frequentadores desorganizados: "))
    total_organizados = total_pessoas - total_desorganizados
except ValueError:
    print("Por favor, insira valores válidos!")
    exit()

# Inicializa o simulador
simulador = SmartFitSimulator(halteres_padrao, total_organizados, total_desorganizados)

# Cronometrar execução
start = time.time()

# Executa as simulações
print("Executando simulações...")
resultados, media_desordem, desvio_padrao, intervalo_confianca = simulador.executa_simulacoes(num_simulacoes)
print(f"Simulações concluídas em {time.time() - start:.2f} segundos.")

# Exibe os resultados
print(f"\nResultados das Simulações:")
print(f"Média de desordem: {media_desordem:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Intervalo de confiança (95%): {intervalo_confianca}")

# Plota os gráficos
start = time.time()
print("Gerando o histograma da desordem...")
plot_histograma(resultados)
print(f"Histograma gerado em {time.time() - start:.2f} segundos.")

start = time.time()
print("Calculando o impacto da proporção de desorganizados...")
plot_impacto_porcentagem(halteres_padrao, total_pessoas, num_simulacoes)
print(f"Gráfico de impacto gerado em {time.time() - start:.2f} segundos.")

# Pausa no final para manter o terminal aberto
input("\nPressione Enter para encerrar o programa.")
