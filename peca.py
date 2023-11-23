from config import *
import random

class Bloco(pg.sprite.Sprite):
    def __init__(self, tetramino, posicao):
        self.tetramino = tetramino
        self.posicao = vetor(posicao) + INIT_POS_OFFSET
        self.proxima_posicao = vetor(posicao) + NEXT_POS_OFFSET
        self.vivo = True

        super().__init__(tetramino.tetris.sprite_group)

        #cria o atributo "image" para receber a cor, chamando o "TILE_SIZE" para definir o tamanho que a peça será
        self.image = tetramino.image
        #self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        #pg.draw.rect(self.image, "pink", (1,1, TILE_SIZE - 2, TILE_SIZE - 2), border_radius = 8)

        self.rect = self.image.get_rect()

    def se_vivo(self):
        if not self.vivo:
            self.kill()

    def rotacionar(self, trocar_posicao):
        translacao = self.posicao - trocar_posicao
        rotacao = translacao.rotate(90)
        return rotacao + trocar_posicao

    def posicao_rect(self):
        posicao = [self.proxima_posicao, self.posicao][self.tetramino.current]
        self.rect.topleft = posicao * TILE_SIZE

    def update(self):
        self.se_vivo()
        self.posicao_rect()

    #define a codição para a colisão com o chão
    def colidir(self, posicao):
        x, y = int(posicao.x), int(posicao.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetramino.tetris.array_tela[y][x]):
            return False
        return True

class Tetramino:
    def __init__(self, tetris, current = True):
        self.tetris = tetris
        self.forma = random.choice(list(TETRAMINOS.keys()))
        self.image = random.choice(tetris.app.imagens)
        self.bloco = [Bloco(self, posicao) for posicao in TETRAMINOS[self.forma]]
        self.parar = False
        self.current = current

    def rotacionar(self):
        trocar_posicao = self.bloco[0].posicao
        nova_posicao = [bloco.rotacionar(trocar_posicao) for bloco in self.bloco]

        if not self.colidir(nova_posicao):
            for i, bloco in enumerate (self.bloco):
                bloco.posicao = nova_posicao[i]

    #faz com que qualquer um dos tetraminos colida com o chão não importa sua posição
    def colidir(self, posicao_bloco):
        return any(map(Bloco.colidir, self.bloco, posicao_bloco))

    #condição para os tetraminos se moverem com os comandos definidos 
    def mover(self, direcao):
        mover = MOVE_DIRECTIONS[direcao]
        nova_posicao = [bloco.posicao + mover for bloco in self.bloco]
        colidir = self.colidir(nova_posicao)

        if not colidir:
            for bloco in self.bloco:
                bloco.posicao += mover
        elif direcao == "baixo":
            self.parar = True


    def update(self):
        self.mover(direcao = "baixo")
        