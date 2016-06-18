from mapa import *

# constantes representando as cores
MARRON = (94, 71, 39)
VERDE = (34, 139, 34)
AZUL = (0, 51, 102)
CINZA_ESC = (128, 128, 128)
CINZA_CLA = (190, 190, 190)
VERMELHO = (255, 0, 0)
AMARELO = (255,255,0)

# um dicionario representando as cores
cores = {
    T: MARRON,
    A: CINZA_ESC,
    G: VERDE,
    E: AZUL,
    P: CINZA_CLA,
    C: VERMELHO
}

# um dicionario representando os pesos
pesos = {
    T: 3,
    A: 1,
    G: 5,
    P: 10,
    E: float('inf')
}

# dimensoes do jogo
TAM_QUAD = 15
LARGURA_MAPA = len(mapa[0])
ALTURA_MAPA = len(mapa)

def adp_vizinhos(no):
    vizi = []
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for dir in dirs:
        neighbor = (no[0] + dir[0], no[1] + dir[1])
        if 0 <= no[0] < 42 and 0 <= no[1] < 42:
            vizi.append(neighbor)
    return vizi


def vizinhos(pos):
    v = []
    if pos[0] > 0:
        v.append((pos[0] - 1, pos[1]))
    if pos[1] > 0:
        v.append((pos[0], pos[1] - 1))
    if pos[0] < 41:
        v.append((pos[0] + 1, pos[1]))
    if pos[1] < 41:
        v.append((pos[0], pos[1] + 1))
    return v

def heuristica(a, b):
   #Manhattan distance on a square grid
   return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_estrela(inicio, final):
    nova_pos = ()
    abertos = [inicio]
    fechados = []
    f = {} # soma heuristica + g
    g = {inicio: 0} # soma dos pesos
    veio_de = {}
    f[inicio] = g[inicio] + heuristica(inicio, final)

    while len(abertos) > 0:
        abertos.sort(key=f.get, reverse=True)
        posicao = abertos.pop()
        if posicao == final:
            return g[final], veio_de
        fechados.append(posicao)
        for v in vizinhos(posicao):
            if fechados.count(v) == 0:
                g_de_v = g[posicao] + pesos[mapa[v[1]][v[0]]]
                if abertos.count(v) == 0 or g_de_v < g[v]:
                    veio_de[v] = posicao
                    g[v] = g_de_v
                    f[v] = g_de_v + heuristica(v, final)
                    if abertos.count(v) == 0:
                        abertos.append(v)

    #return nova_pos