T = 0
A = 1
G = 2
E = 3
P = 4
C = 5
M= 6

mapa = [
    [G for l in range(42)],
    [G for l in range(42)],
    [G, G, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, G, G],
    [G, G, E, G, G, G, G, G, G, G, G, G, G, G, G, G, G, A, T, T, T, A, G, G, G, P, P, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, G, G, G, A, A, A, A, A, A, A, A, A, A, A, A, T, T, T, A, G, G, G, P, G, G, G, G, G, G, G, G, G, G, G, G, P, E, G, G],
    [G, G, E, G, G, G, A, E, E, E, A, A, E, E, E, A, G, A, T, T, T, A, A, A, A, P, G, T, T, T, T, T, T, T, T, T, T, G, P, E, G, G],
    [G, G, E, G, G, G, A, E, E, E, E, E, E, E, E, A, G, A, T, T, T, A, A, A, A, P, G, T, T, T, T, T, T, T, T, T, T, G, P, E, G, G],
    [G, G, E, G, G, G, A, E, E, E, E, E, E, E, E, A, G, A, T, T, T, A, G, G, G, P, G, G, G, G, G, G, G, G, G, G, G, G, P, E, G, G],
    [G, G, E, G, G, G, A, E, E, E, E, E, E, E, E, A, G, A, T, T, T, A, G, G, G, P, P, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, A, A, A, A, A, A, A, A, A, A, A, A, A, G, A, T, T, T, A, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, E, G, G],
    [G, G, E, A, P, P, P, P, P, P, P, P, P, G, G, G, G, A, T, T, T, A, G, G, G, E, E, E, E, E, E, E, E, E, E, G, G, G, G, E, G, G],
    [G, G, E, A, P, E, E, E, P, E, E, E, P, G, G, G, G, A, T, T, T, A, A, A, A, A, A, A, A, A, A, A, A, A, E, G, G, G, G, E, G, G],
    [G, G, E, A, P, P, E, P, P, E, P, E, P, A, A, A, A, A, T, T, T, A, G, G, G, G, E, E, E, E, E, E, E, A, E, G, G, G, G, E, G, G],
    [G, G, E, A, P, P, E, P, P, E, E, E, P, A, A, A, A, A, T, T, T, A, G, G, G, G, E, E, E, E, E, A, A, A, E, G, G, G, G, E, G, G],
    [G, G, E, A, P, E, E, E, P, E, P, E, P, G, G, G, G, A, T, T, T, A, G, G, G, G, E, E, E, E, E, E, E, P, E, G, G, G, G, E, G, G],
    [G, G, E, A, P, P, P, P, P, P, P, P, P, G, G, G, G, A, T, T, T, A, A, A, A, P, P, P, P, P, P, P, P, P, E, G, G, G, G, E, G, G],
    [G, G, E, T, T, T, T, T, T, T, T, T, T, T, T, G, G, A, T, T, T, A, G, G, G, E, E, E, E, E, E, E, E, E, E, G, G, G, G, E, G, G],
    [G, G, E, T, T, T, T, T, T, T, T, T, T, T, T, G, G, A, T, T, T, A, G, G, G, T, T, T, T, T, T, T, T, T, T, T, T, T, T, E, G, G],
    [G, G, E, T, T, P, P, P, P, P, P, P, P, P, P, G, G, A, T, T, T, A, G, G, G, T, T, T, T, T, T, T, T, T, T, T, T, T, T, E, G, G],
    [G, G, E, T, T, P, E, E, E, E, E, E, E, E, P, G, G, A, T, T, T, A, G, G, G, T, T, E, E, E, E, E, E, E, E, E, E, E, T, E, G, G],
    [G, G, E, T, T, P, E, E, E, E, E, E, P, P, P, A, A, A, T, T, T, A, A, A, A, T, T, E, E, E, E, E, E, E, E, E, E, E, T, E, G, G],
    [G, G, E, T, T, P, E, E, E, E, E, E, P, P, P, A, A, A, T, T, T, A, A, A, A, T, T, E, E, E, E, E, E, E, E, E, E, E, T, E, G, G],
    [G, G, E, T, T, P, E, E, E, E, E, E, E, E, P, G, G, A, T, T, T, A, G, G, G, T, T, E, E, E, E, E, P, E, E, E, E, E, T, E, G, G],
    [G, G, E, T, T, P, P, P, P, P, P, P, P, P, P, G, G, A, T, T, T, A, G, G, G, T, T, T, T, T, T, T, P, T, T, T, T, T, T, E, G, G],
    [G, G, E, T, T, T, T, T, T, T, T, T, T, T, T, G, G, A, T, T, T, A, G, G, G, T, T, T, T, T, T, T, P, T, T, T, T, T, T, E, G, G],
    [G, G, E, T, T, T, T, T, T, T, T, T, T, T, T, G, G, A, T, T, T, A, G, G, G, G, G, G, G, G, G, G, P, G, G, G, G, G, G, E, G, G],
    [G, G, E, P, P, P, P, P, P, P, P, P, P, P, P, G, G, A, A, A, A, A, G, G, G, G, G, G, G, G, G, G, P, G, G, G, G, G, G, E, G, G],
    [G, G, E, P, P, P, P, P, P, P, P, P, P, P, P, G, G, G, G, A, G, G, G, G, G, G, G, G, G, G, G, G, P, G, G, G, G, G, G, E, G, G],
    [G, G, E, P, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, G, E, E, E, E, E, E, E, E, A, A, A, P, A, A, A, A, A, A, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, G, G, G, G, G, G, A, G, E, E, E, E, E, E, A, A, A, A, A, P, A, A, A, A, A, A, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, G, G, G, G, G, G, A, G, E, E, E, E, E, E, A, A, A, A, A, P, A, A, A, A, A, A, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, G, G, G, G, G, A, A, G, E, E, E, E, E, E, E, E, A, A, A, P, A, A, A, A, A, A, E, G, G],
    [G, G, E, P, A, P, P, A, A, E, E, E, P, G, G, G, G, G, A, E, G, G, G, G, G, G, T, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, A, A, A, A, A, A, E, G, G, G, G, G, G, T, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, A, E, E, E, E, E, E, G, G, G, G, G, G, T, T, T, E, E, E, E, E, E, E, T, T, P, E, G, G],
    [G, G, E, P, A, P, P, E, E, E, E, E, P, A, G, G, G, G, G, G, G, G, G, G, G, G, T, T, T, E, E, E, E, E, E, P, P, P, P, E, G, G],
    [G, G, E, P, A, P, P, P, P, P, P, P, P, A, A, A, A, A, A, A, A, A, A, A, A, A, T, T, T, E, E, E, E, E, E, E, T, T, P, E, G, G],
    [G, G, E, P, A, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, A, G, G, G, G, T, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, P, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, P, A, G, G, G, G, T, P, P, P, P, P, P, P, P, P, P, P, P, E, G, G],
    [G, G, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, P, A, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, G, G],
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, P, A, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, P, A, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G]
]

