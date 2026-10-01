import pyxel

class Jogo:
    def __init__(self):
        pyxel.init(128, 128, title="Meu Celeste", fps=60)
        self.x = 20.0
        self.y = 100.0
        self.vx = 0.0
        self.vy = 0.0
        self.no_chao = False
        pyxel.run(self.update, self.draw)

    def update(self):
        #movimento horizontal
        if pyxel.btn(pyxel.KEY_LEFT):
            self.vx = -1.5
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.vx = 1.5
        else:
            self.vx = 0

        #pulo
        if self.no_chao and pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -4

        #gravidade
        self.vy += 0.3

        self.x += self.vx
        self.y += self.vy

        #chao
        if self.y >= 112:
            self.y = 112
            self.vy = 0
            self.no_chao = True
        else:
            self.no_chao = False

    def draw(self):
        pyxel.cls(1)
        pyxel.rect(0, 120, 128, 8, 3)                  #chao
        pyxel.rect(int(self.x), int(self.y), 8, 8, 8)  #boneco

Jogo()