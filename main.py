from config import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set.caption("Tetris")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def desenhar(self):
        self.screen.fill(color = FIELD_COLOR)
        self.tetris.desenhar()
        pg.display.flip()

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    #faz o aplicativo do jogo rodar, chamando as funções principais
    def rodar(self): 
        while True:
            self.eventos()
            self.update()
            self.desenhar()