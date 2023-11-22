from config import *
import math
from peca import Tetramino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetramino = Tetramino(self)

    def controles(self, tecla_pressionada):
        if tecla_pressionada == pg.K_LEFT:
            self.tetramino.mover(direcao = "esquerda")
        elif tecla_pressionada == pg.K_RIGHT:
            self.tetramino.mover(direcao = "direita")
    
    def desenhar_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    def update(self):
        if self.app.anim_trigger:
            self.tetramino.update()
        self.sprite_group.update()
    
    def desenhar(self):
        self.desenhar_grid()
        self.sprite_group.draw(self.app.screen)