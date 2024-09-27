'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 15: técnicas de programação IMPACTA 27 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳
→ Qual é o custo computacional (de acordo com a notação Big O) de uma função que implementa o algoritmo de busca binária?
→ A resposta anterior depende dos valores passados para os parâmetros da função?
'''
# complexidade de algoritmo logarítmica O (log n)
# logaritmo de base 2 .

# %% ---> begin
# imports
import random
import numpy as np
import matplotlib.pyplot as plt

# funções
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    passos=0 # variavel contadora

    while inicio <= fim:
        passos+=1 # variavel contadora cada instruções será executada
        meio = (inicio + fim) // 2 

        if lista[meio] == valor:
            return meio, passos
        
        elif lista[meio] > valor:
            fim = meio - 1
        
        else:
            inicio = meio + 1

    return -1, passos

def criar_lista_aleatoria(tamanho, inicio, fim):
    lista = [random.randint(inicio, fim) for _ in range(tamanho)]
    return lista


# programa principal
# TODO: criar diferentes sequências, todas ordenadas, com tamanhos distintos
# TODO: busca binaria por um valor que não está presente na sequência
# Traçar um gráfico len(lista)x quantidade de passos



# %% ---> end
