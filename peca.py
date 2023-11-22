from config import *
import random

class Bloco(pg.sprite.Sprite):
    def __init__(self, tetramino, posicao):
        self.tetramino = tetramino
        self.posicao = vetor(posicao) + INIT_POS_OFFSET

        super().__init__(tetramino.tetris.sprite_group)

        #cria o atributo "image" para receber a cor, chamando o "TILE_SIZE" para definir o tamanho que a peça será
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('pink')

        self.rect = self.image.get_rect()

    def posicao_rect(self):
        self.rect.topleft = self.posicao * TILE_SIZE

    def update(self):
        self.posicao_rect()

class Tetramino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.forma = random.choice(list(TETRAMINOS.keys()))
        self.bloco = [Bloco(self, posicao) for posicao in TETRAMINOS[self.forma]]

    def mover(self, direcao):
        mover = MOVE_DIRECTIONS[direcao]
        for bloco in self.bloco:
            bloco.posicao += mover

    def update(self):
        self.mover(direcao = "baixo")
        