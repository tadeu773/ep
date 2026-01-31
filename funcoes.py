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
def verifica_ganhador(jogadores):
    for jogador in jogadores:
        if len(jogadores[jogador]) == 0:
            return jogador
    return -1
def conta_pontos(pecas):
    total = 0
    for peca in pecas:
        total += peca[0] + peca[1]
    return total
def posicoes_possiveis(mesa, pecas):
    posicoes = []
    if mesa == []:
        for i in range(len(pecas)):
            posicoes.append(i)
        return posicoes
    ponta_esq = mesa[0][0]
    ponta_dir = mesa[-1][1]
    for i in range(len(pecas)):
        peca = pecas[i]
        if peca[0] == ponta_esq or peca[1] == ponta_esq or \
           peca[0] == ponta_dir or peca[1] == ponta_dir:
            posicoes.append(i)
    return posicoes
