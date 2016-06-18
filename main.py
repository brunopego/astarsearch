from util import *
import pygame
from pygame.locals import *
import sys

# Para executar a busca pressione ENTER ate chegar a saida do labirinto

coleguinha = 0
coleguinhas = [(32, 5), (31, 13), (35, 35), (8, 32)]
#coleguinhas = [(12, 20)]
saidas = [(20, 41), (21, 41)]

def desenha():
    for linha in range(ALTURA_MAPA):
        for coluna in range(LARGURA_MAPA):
            pygame.draw.rect(tela, cores[mapa[linha][coluna]], (coluna * TAM_QUAD, linha * TAM_QUAD, TAM_QUAD, TAM_QUAD))
    for i in range(coleguinha, len(coleguinhas)):
        pygame.draw.rect(tela, AMARELO, (coleguinhas[i][0] * TAM_QUAD, coleguinhas[i][1] * TAM_QUAD, TAM_QUAD, TAM_QUAD))


def desenha_caminho(caminho, inicio, final):
    posicao = final
    while posicao != inicio:
        pygame.draw.rect(tela, cores[C], (posicao[0] * TAM_QUAD, posicao[1] * TAM_QUAD, TAM_QUAD, TAM_QUAD))
        #print(posicao)
        posicao = caminho[posicao]
    pygame.draw.rect(tela, cores[C], (posicao[0] * TAM_QUAD, posicao[1] * TAM_QUAD, TAM_QUAD, TAM_QUAD))

if __name__ == "__main__":
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_MAPA * TAM_QUAD, ALTURA_MAPA * TAM_QUAD))
    pygame.display.set_caption('Inteligência Artificial')

    # Adicionando jogador
    PLAYER = pygame.image.load('ball-15.png').convert_alpha()
    player_pos = (12, 20)

    desenha()
    tela.blit(PLAYER, (player_pos[0] * TAM_QUAD, player_pos[1] * TAM_QUAD))


    #a_estrela(player_pos, final)

    custo_total = 0
    saiu = False
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    print(player_pos)
                    if coleguinha < len(coleguinhas):
                        final = coleguinhas[coleguinha]
                        custo, caminho = a_estrela(player_pos, final)
                        custo_total += custo
                        print('Custo total: '+str(custo_total))
                        desenha()
                        desenha_caminho(caminho, player_pos, final)
                        player_pos = final
                        tela.blit(PLAYER, (player_pos[0] * TAM_QUAD, player_pos[1] * TAM_QUAD))
                        coleguinha = coleguinha + 1
                    else:
                        if not saiu:
                            melhor = float('inf')
                            for saida in saidas:
                                custo, caminho = a_estrela(player_pos, saida)
                                if custo < melhor:
                                    melhor = custo
                                    melhor_caminho = caminho
                                    melhor_saida = saida
                            custo_total += melhor
                            print('Custo total: '+str(custo_total))
                            desenha()
                            desenha_caminho(melhor_caminho, player_pos, melhor_saida)
                            player_pos = saida
                            tela.blit(PLAYER, (player_pos[0] * TAM_QUAD, player_pos[1] * TAM_QUAD))

        # atualiza a tela
        pygame.display.update()
