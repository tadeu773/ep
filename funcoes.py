import random

def cria_pecas():
    pecas = []

    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])

    random.shuffle(pecas)
    return pecas
def inicia_jogo(n_jogadores, pecas):
    jogadores = {}
    for i in range(n_jogadores):
        inicio = i * 7
        fim = inicio + 7
        jogadores[i] = pecas[inicio:fim]
    monte = pecas[n_jogadores * 7:]
    return {
        'jogadores': jogadores,
        'monte': monte,
        'mesa': []
    }