import pyxel

class Jogo:
    def __init__(self):
        pyxel.init(256, 144, title="Pyleste", fps=60, display_scale=6)
        pyxel.load("assets.pyxres")
        self.direcao = -1
        self.x = pyxel.width // 2 - 4
        self.y = pyxel.height - 16
        self.vx = 0.0
        self.vy = 0.0
        self.no_chao = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.vx = -1
            self.direcao = 1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.vx = 1
            self.direcao = -1
        else:
            self.vx = 0
        
        if self.no_chao and pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -3.5
        self.vy += 0.3
        self.x += self.vx
        self.y += self.vy

        if self.tile_solido(self.x + 4, self.y + 8):
            self.y = (int(self.y + 8) // 8) * 8 - 8
            self.vy = 0
            self.no_chao = True
        else:
            self.no_chao = False

        if self.y >= pyxel.height - 16:
            self.y = pyxel.height - 16
            self.vy = 0
            self.no_chao = True
        else:
            self.no_chao = False

    def draw(self):
        pyxel.cls(1)
        pyxel.bltm(0, 0, 0, 0, -16, pyxel.width, pyxel.height, 0)              
        if self.no_chao and self.vx != 0:
            quadro = (pyxel.frame_count // 6) % 2
            u = 8 + (quadro * 8) 
        else:
            u = 8
        pyxel.blt(int(self.x), int(self.y), 0, u, 0, 8 * self.direcao, 8, 0)

    def tile_solido(self, x, y):
        tx = int(x // 8)
        ty = int(y // 8)
        tile = pyxel.tilemaps[0].pget(tx, ty)
        return tile != (0, 0)   
Jogo()