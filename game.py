import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("assets/image_map.pyxres")
        self.position = {"x": 66, "y": 66}
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=1, period=1):
            self.position["x"] += 1
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, period=1):
            self.position["x"] -= 1
        if pyxel.btnp(pyxel.KEY_UP, hold=1, period=1):
            self.position["y"] -= 1
        if pyxel.btnp(pyxel.KEY_DOWN, hold=1, period=1):
            self.position["y"] += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", 8)
        pyxel.blt(self.position["x"], self.position["y"], 0, 9, 0, 6, 7)


App()
