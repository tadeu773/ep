import random
from funcoes_domino import *
RESET = "\033[0m"
CORES = {
    0: "\033[37m",
    1: "\033[31m",
    2: "\033[32m",
    3: "\033[33m",
    4: "\033[34m",
    5: "\033[35m",
    6: "\033[36m",
}
def imprime_peca_colorida(peca):
    a, b = peca
    return f"[{CORES[a]}{a}{RESET}|{CORES[b]}{b}{RESET}]"
def imprime_mesa(mesa):
    print("\nMESA:")
    if mesa == []:
        print("[]")
    else:
        for p in mesa:
            print(imprime_peca_colorida(p), end=" ")
        print()
def imprime_pecas_jogador(pecas, possiveis, ultima_comprada):
    for i in range(len(pecas)):
        if i in possiveis:
            print("  *  ", end="")
        else:
            print("     ", end="")
    print()
    for p in pecas:
        print(imprime_peca_colorida(p), end=" ")
    print()
    for i, p in enumerate(pecas):
        if p == ultima_comprada:
            print("     ", end="")
        else:
            print(f"  {i+1}  ", end="")
    print()
print("Bem-vindo(a) ao jogo de Dominó!")
print("O objetivo é ficar sem peças antes dos outros jogadores.\n")
while True:
    try:
        n = int(input("Quantos jogadores? (2-4) "))
        if 2 <= n <= 4:
            break
        print("Número inválido!")
    except:
        print("Entrada inválida!")
pecas = cria_pecas()
estado = inicia_jogo(n, pecas)
jogadores = estado["jogadores"]
mesa = estado["mesa"]
monte = estado["monte"]
jogador_atual = random.randint(0, n - 1)
while True:
    imprime_mesa(mesa)
    pecas_jogador = jogadores[jogador_atual]
    possiveis = posicoes_possiveis(mesa, pecas_jogador)
    ultima_comprada = None
    jogou = False
    print(f"\nJogador {jogador_atual} com {len(pecas_jogador)} peça(s)")
    if jogador_atual == 0:
        imprime_pecas_jogador(pecas_jogador, possiveis, ultima_comprada)
        if possiveis == []:
            print("Nenhuma jogada possível.")
            if monte != []:
                input("Pressione ENTER para comprar do monte...")
                ultima_comprada = monte.pop(0)
                pecas_jogador.append(ultima_comprada)
            else:
                print("Monte vazio. Passa a vez.")
        else:
            while True:
                escolha = input("Escolha a posição da peça: ")
                if not escolha.isdigit():
                    print("Entrada inválida!")
                    continue
                escolha = int(escolha) - 1
                if escolha in possiveis:
                    peca = pecas_jogador.pop(escolha)
                    mesa = adiciona_na_mesa(peca, mesa)
                    print(f"Você colocou {imprime_peca_colorida(peca)}")
                    jogou = True
                    break
                else:
                    print("Posição inválida!")
    else:
        if possiveis == []:
            if monte != []:
                pecas_jogador.append(monte.pop(0))
        else:
            escolha = random.choice(possiveis)
            peca = pecas_jogador.pop(escolha)
            mesa = adiciona_na_mesa(peca, mesa)
            print(f"Jogador {jogador_atual} colocou {imprime_peca_colorida(peca)}")
            jogou = True
    if jogou:
        vencedor = verifica_ganhador(jogadores)
        if vencedor != -1:
            print("\nFIM DE JOGO!")
            for j in jogadores:
                pontos = conta_pontos(jogadores[j])
                print(f"Jogador {j}: {pontos} pontos")
            print(f"\nVENCEDOR: Jogador {vencedor}")
            break
    jogador_atual = (jogador_atual + 1) % n
    
