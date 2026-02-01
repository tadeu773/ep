import random
from funcoes_domino import *
def imprime_mesa(mesa):
    print("\nMESA:")
    if mesa == []:
        print("[]")
    else:
        for p in mesa:
            print(f"[{p[0]}|{p[1]}]", end=" ")
        print()
def imprime_pecas_jogador(pecas):
    for i, p in enumerate(pecas):
        print(f"[{p[0]}|{p[1]}]", end=" ")
    print()
    for i in range(len(pecas)):
        print(f"  {i+1} ", end=" ")
    print()
print("Bem-vindo(a) ao jogo de Dominó!")
print("O objetivo é ficar sem peças antes dos outros jogadores.\n")
while True:
    n = int(input("Quantos jogadores? (2-4) "))
    if 2 <= n <= 4:
        break
    print("Número inválido!")
pecas = cria_pecas()
estado = inicia_jogo(n, pecas)
jogadores = estado['jogadores']
monte = estado['monte']
mesa = estado['mesa']
jogador_atual = random.randint(0, n-1)
while True:
    imprime_mesa(mesa)
    pecas_jogador = jogadores[jogador_atual]
    print(f"\nJogador {jogador_atual} com {len(pecas_jogador)} peça(s)")
    possiveis = posicoes_possiveis(mesa, pecas_jogador)
    if jogador_atual == 0:
        imprime_pecas_jogador(pecas_jogador)
        if possiveis == []:
            if monte != []:
                print("Sem jogadas possíveis. Comprando do monte...")
                pecas_jogador.append(monte.pop(0))
            else:
                print("Sem jogadas possíveis e sem monte. Passa a vez.")
        else:
            while True:
                escolha = int(input("Escolha a peça: ")) - 1
                if escolha in possiveis:
                    break
                print("Posição inválida!")
            peca = pecas_jogador.pop(escolha)
            mesa = adiciona_na_mesa(peca, mesa)
            print(f"Colocou: [{peca[0]}|{peca[1]}]")
    else:
        if possiveis == []:
            if monte != []:
                pecas_jogador.append(monte.pop(0))
            else:
                pass
        else:
            escolha = random.choice(possiveis)
            peca = pecas_jogador.pop(escolha)
            mesa = adiciona_na_mesa(peca, mesa)
            print(f"Jogador {jogador_atual} colocou [{peca[0]}|{peca[1]}]")
    vencedor = verifica_ganhador(jogadores)
    if vencedor != -1:
        print("\nFIM DE JOGO!")
        for j in jogadores:
            pontos = conta_pontos(jogadores[j])
            print(f"Jogador {j}: {pontos} pontos")
        print(f"\nVENCEDOR: Jogador {vencedor}")
        break
    jogador_atual = (jogador_atual + 1) % n
