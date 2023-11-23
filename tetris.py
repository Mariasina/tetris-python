#importa as bibliotecas e arquivos necessários para o jogo rodar"
from config import *
import math
from peca import Tetramino
import pygame.freetype as ft

#define a classe para que escrever textos dentro do jogo com a fonte escolhida
class Texto:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def desenhar(self):
        self.font.render_to(self.app.tela, (WIN_W * 0.595, WIN_H * 0.05), text = "TETRIS", fgcolor = "white", size = TILE_SIZE * 1.28)
        self.font.render_to(self.app.tela, (WIN_W * 0.630, WIN_H * 0.28), text = "Proxima:", fgcolor = "white", size = TILE_SIZE * 1.00)
        self.font.render_to(self.app.tela, (WIN_W * 0.655, WIN_H * 0.65), text = "Score:", fgcolor = "white", size = TILE_SIZE * 1.00)
        self.font.render_to(self.app.tela, (WIN_W * 0.68, WIN_H * 0.75), text = f"{self.app.tetris.score}", fgcolor = "white", size = TILE_SIZE * 0.90)
    
class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.array_tela = self.criar_array_tela()
        self.tetramino = Tetramino(self)
        self.proximo_tetramino = Tetramino(self, current = False)
        self.acelerar = False

        self.score = 0
        self.linhas_completas = 0
        self.pontos_linha = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    #define 
    def get_score(self):
        self.score += self.pontos_linha[self.linhas_completas]
        self.linhas_completas = 0

    def checar_linhas_cheias(self):
        row = FIELD_H - 1
        for y in range(FIELD_H -1, -1, -1):
            for x in range(FIELD_W):
                self.array_tela[row][x] = self.array_tela[y][x]

                if self.array_tela[y][x]:
                    self.array_tela[row][x].posicao = vetor(x, y)

            if sum(map(bool, self.array_tela[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.array_tela[row][x].vivo = False
                    self.array_tela[row][x] = 0

                self.linhas_completas += 1
            
    def colocar_tetromino_array(self):
        for bloco in self.tetramino.bloco:
            x, y = int(bloco.posicao.x), int(bloco.posicao.y)
            self.array_tela[y][x] = bloco

    def criar_array_tela(self):
        return[[0 for x in range(FIELD_W)] for y in range (FIELD_H)]
    
    def game_over(self):
        if self.tetramino.bloco[0].posicao.y == INIT_POS_OFFSET[1]:
            pg.time.wait(1000)
            return True

    def checar_parada_tetramino(self):
        if self.tetramino.parar:
            if self.game_over():
                self.__init__(self.app)
            else:
                self.acelerar = False
                self.colocar_tetromino_array()
                self.proximo_tetramino.current = True
                self.tetramino = self.proximo_tetramino
                self.proximo_tetramino = Tetramino(self, current = False)

    def controles(self, tecla_pressionada):
        if tecla_pressionada == pg.K_LEFT:
            self.tetramino.mover(direcao = "esquerda")
        elif tecla_pressionada == pg.K_RIGHT:
            self.tetramino.mover(direcao = "direita")
        elif tecla_pressionada == pg.K_UP:
            self.tetramino.rotacionar()
        elif tecla_pressionada == pg.K_DOWN:
            self.acelerar = True
    
    def desenhar_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.tela, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.acelerar]
        if trigger:
            self.checar_linhas_cheias()
            self.tetramino.update()
            self.checar_parada_tetramino()
            self.get_score()
        self.sprite_group.update()
    
    def desenhar(self):
        self.desenhar_grid()
        self.sprite_group.draw(self.app.tela)