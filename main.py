from config import *
from tetris import Tetris
import sys

class App:
    #método construtor para criar os atributos da classe
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

    def set_timer(self):
        self.user_event = pg.USEREVENT = 0
        self.anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    #método para dar "update" no app jogo a cada tick, que serão 60 frames por segundo
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    #método para pintar o fundo do app com a cor definida em "FIELD_COLOR"
    def desenhar(self):
        self.screen.fill(color = FIELD_COLOR)
        self.tetris.desenhar()
        pg.display.flip()

    #método que checa os eventos do jogo
    def eventos(self):
        self.anim_trigger = False
        for event in pg.event.get():
            #caso seja pressionado o botão "ESC" ou o botão de fechar seja clicado o jogo se fecha
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.controles(tecla_pressionada = event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True

    #faz o aplicativo do jogo rodar, chamando as funções principais
    def rodar(self): 
        while True:
            self.eventos()
            self.update()
            self.desenhar()


game = App()

game.rodar()