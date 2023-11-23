import pygame as pg

vetor = pg.math.Vector2

#configurações gerais do jogo
FPS = 60

#define a cor de fundo
FIELD_COLOR = (196, 59, 109)
BG_COLOR = (46, 45, 45)

SPRITE_DIR_PATH = "sprites"
FONT_PATH = "font/04B_30__.ttf"

ANIM_TIME_INTERVAL = 200
FAST_ANIM_TIME_INTERVAL = 15

#define o tamanho de cada bloco que será mostrado em pixels
TILE_SIZE = 35

#define o tamanho que a tela terá tanto verticalmente quanto horizontalmente
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W  * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vetor(FIELD_W // 2 - 1,0)
NEXT_POS_OFFSET = vetor(FIELD_W * 1.3, FIELD_H * 0.45)

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