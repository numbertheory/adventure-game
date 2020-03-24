import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.position = {"x": 66, "y": 66}
        self.direction = "left"
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=1, period=1):
            self.direction = "right"
            self.position["x"] += 1
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, period=1):
            self.direction = "left"
            self.position["x"] -= 1
        if pyxel.btnp(pyxel.KEY_UP, hold=1, period=1):
            self.direction = "up"
            self.position["y"] -= 1
        if pyxel.btnp(pyxel.KEY_DOWN, hold=1, period=1):
            self.direction = "down"
            self.position["y"] += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Dungeon DOS", 8)
        if self.direction == "left":
            pyxel.blt(self.position["x"],
                      self.position["y"], 0, 9, 0, 6, 7, colkey=1)
        elif self.direction == "right":
            pyxel.blt(self.position["x"],
                      self.position["y"], 0, 17, 0, 6, 7, colkey=1)
        elif self.direction == "up":
            pyxel.blt(self.position["x"],
                      self.position["y"], 0, 33, 0, 6, 7, colkey=1)
        elif self.direction == "down":
            pyxel.blt(self.position["x"],
                      self.position["y"], 0, 25, 0, 6, 7, colkey=1)


App()
