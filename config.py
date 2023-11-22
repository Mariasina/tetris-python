import pygame as pg

vetor = pg.math.Vector2

#configurações gerais do jogo
FPS = 60

#define a cor de fundo
FIELD_COLOR = (48, 39, 32)

ANIM_TIME_INTERVAL = 150

#define o tamanho de cada bloco que será mostrado em pixels
TILE_SIZE = 50

#define o tamanho que a tela terá tanto verticalmente quanto horizontalmente
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W  * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vetor(FIELD_W // 2 - 1,0)

MOVE_DIRECTIONS = {"esquerda": vetor(-1,0), "direita": vetor(1,0), "baixo": vetor(0,1)}

#define um dicionario para informar o formato de cada peca que será utilizada no jogo
TETRAMINOS = {
    "T": [(0,0),(-1,0),(1,0),(0,-1)],
    "O": [(0,0),(0,-1),(1,0),(1,-1)],
    "J": [(0,0),(-1,0),(0,-1),(0,-2)],
    "L": [(0,0),(1,0),(0,-1),(0,-2)],
    "I": [(0,0),(0,1),(0,-1),(0,-2)],
    "S": [(0,0),(-1,0),(0,-1),(1,-1)],
    "Z": [(0,0),(1,0),(0,-1),(-1,-1)],
}