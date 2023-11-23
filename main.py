#importa as bibliotecas e arquivos necessários para o jogo rodar
from config import *
from tetris import Tetris, Texto
import sys
import pathlib

class App:
    #método construtor para criar os atributos da classe
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.tela = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.contador()
        self.imagens = self.carregar_imagem()
        self.tetris = Tetris(self)
        self.texto = Texto(self)

    #carrega os sprites para os tetraminos
    def carregar_imagem(self):
        arquivos = [item for item in pathlib.Path(SPRITE_DIR_PATH).glob("*.png") if item.is_file()]
        imagens = [pg.image.load(file).convert_alpha() for file in arquivos]
        imagens = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in imagens]
        return imagens

    #define um contador para contar quão rápido as peças irão cair
    def contador(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1

        self.anim_trigger = False
        self.fast_anim_trigger = False

        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    #método para dar "update" no app jogo a cada tick, que serão 60 frames por segundo
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    #método para pintar o fundo do app com a cor definida em "FIELD_COLOR" e "BG_COLOR"
    def desenhar(self):
        self.tela.fill(color = FIELD_COLOR)
        self.tela.fill(color = BG_COLOR, rect = (0, 0, *FIELD_RES))
        self.tetris.desenhar()
        self.texto.desenhar()
        pg.display.flip()

    #método que checa os eventos do jogo
    def eventos(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False

        for event in pg.event.get():
            #caso seja pressionado o botão "ESC" ou o botão de fechar seja clicado o jogo se fecha
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            #chama a função que faz com que a tecla para baixo faça com que a peça desca mais rápido
            #caso não seja pressionada, a peça desse em velocidade normal
            elif event.type == pg.KEYDOWN:
                self.tetris.controles(tecla_pressionada = event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    #faz o aplicativo do jogo rodar, chamando as funções principais
    def rodar(self): 
        while True:
            self.eventos()
            self.update()
            self.desenhar()


game = App()

game.rodar()