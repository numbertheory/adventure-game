import pyxel
import sys


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.position = {"x": 66, "y": 66}
        self.direction = "left"
        pyxel.run(self.update, self.draw)

    def draw_main_character(self):
        sprite = {"left": 9, "right": 17,
                  "up": 33, "down": 25}
        sys.stdout.write("\rx :{}, y:{}".format(
            self.position["x"], self.position["y"]))
        sys.stdout.flush()
        pyxel.blt(self.position["x"],
                  self.position["y"], 0,
                  sprite[self.direction], 0, 6, 7, colkey=1)

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
        self.draw_main_character()


App()
