import pyxel
import sys


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.position = {"x": 66, "y": 66}
        self.direction = "left"
        pyxel.run(self.update, self.draw)

    def log_handler(self, text):
        sys.stdout.write("\r {}".format(str(text)))
        sys.stdout.flush()

    def collision_detect(self):
        border_color = 13
        north_color_bar = []
        south_color_bar = []
        east_color_bar = []
        west_color_bar = []
        for i in range(0, 6):
            north_color_bar.append(
                pyxel.pget(self.position["x"] + i, self.position["y"] - 1)
                )
            south_color_bar.append(
                pyxel.pget(self.position["x"] + i, self.position["y"] + 7)
            )
        for i in range(0, 7):
            east_color_bar.append(
                pyxel.pget(self.position["x"] + 6, self.position["y"] + i)
            )
            west_color_bar.append(
                pyxel.pget(self.position["x"] - 1, self.position["y"] + i)
            )
        if self.direction == "left":
            if border_color in west_color_bar:
                return True
            else:
                return False
        if self.direction == "right":
            if border_color in east_color_bar:
                return True
            else:
                return False
        if self.direction == "up":
            if border_color in north_color_bar:
                return True
            else:
                return False
        if self.direction == "down":
            if border_color in south_color_bar:
                return True
            else:
                return False

    def draw_stone_obstacle(self, x, y):
        pyxel.blt(x, y, 0, 40, 0, 8, 8, colkey=0)

    def draw_main_character(self):
        sprite = {"left": 9, "right": 17,
                  "up": 33, "down": 25}

        pyxel.blt(self.position["x"],
                  self.position["y"], 0,
                  sprite[self.direction], 0, 6, 7, colkey=1)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=1, period=1):
            self.direction = "right"
            if not self.collision_detect():
                self.position["x"] += 1
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, period=1):
            self.direction = "left"
            if not self.collision_detect():
                self.position["x"] -= 1
        if pyxel.btnp(pyxel.KEY_UP, hold=1, period=1):
            self.direction = "up"
            if not self.collision_detect():
                self.position["y"] -= 1
        if pyxel.btnp(pyxel.KEY_DOWN, hold=1, period=1):
            self.direction = "down"
            if not self.collision_detect():
                self.position["y"] += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Dungeon DOS", 8)
        self.draw_main_character()
        # Borders around the playable arena
        for i in range(0, 15):
            self.draw_stone_obstacle(0, i*8)
            self.draw_stone_obstacle(152, i*8)
        for i in range(1, 20):
            self.draw_stone_obstacle(i*8, 0)
            self.draw_stone_obstacle(i*8, 112)


App()
