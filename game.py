import pyxel
import sys
import numpy as np


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.position = {"x": 66, "y": 66}
        self.direction = "left"
        self.mv_boulders = [{"x": 50, "y": 50},
                            {"x": 90, "y": 90},
                            {"x": 50, "y": 90},
                            {"x": 60, "y": 10},
                            {"x": 100, "y": 90},
                            {"x": 120, "y": 90},
                            {"x": 20, "y": 90},
                            {"x": 90, "y": 20}]
        pyxel.run(self.update, self.draw)

    def log_handler(self, text):
        sys.stdout.write("\r {}".format(str(text)))
        sys.stdout.flush()

    def closest_point(self, origin, boulder_coords):
        boulder_coords = np.asarray(boulder_coords)
        boulder_dist = np.sum((boulder_coords - origin)**2, axis=1)
        return np.argmin(boulder_dist)

    def detect_movable_boulder(self, color_bar):
        # Decide which boulder is moving
        boulder_coords = [(x["x"], x["y"]) for x in self.mv_boulders]
        character_coords = (self.position["x"], self.position["y"])
        boulder_id = self.closest_point(character_coords, boulder_coords)
        if self.direction == "up":
            if color_bar != [13, 13, 13, 13, 13, 13]:
                collision_detect = []
                for i in range(0, 6):
                    collision_detect.append(
                        pyxel.pget(self.mv_boulders[boulder_id]["x"] + i,
                                   self.mv_boulders[boulder_id]["y"] - 1))
                if 13 in collision_detect:
                    return True
                else:
                    self.mv_boulders[boulder_id] = {
                        "x": self.mv_boulders[boulder_id]["x"],
                        "y": self.mv_boulders[boulder_id]["y"] - 1
                        }
                    return False

        if self.direction == "down":
            if color_bar != [13, 13, 13, 13, 13, 13]:
                collision_detect = []
                for i in range(0, 7):
                    collision_detect.append(
                        pyxel.pget(self.mv_boulders[boulder_id]["x"] + i,
                                   self.mv_boulders[boulder_id]["y"] + 8))
                if 13 in collision_detect:
                    return True
                self.mv_boulders[boulder_id] = {
                    "x": self.mv_boulders[boulder_id]["x"],
                    "y": self.mv_boulders[boulder_id]["y"] + 1
                    }
                return False

        if self.direction == "left":
            if color_bar != [13, 13, 13, 13, 13, 13, 13]:
                collision_detect = []
                for i in range(0, 7):
                    collision_detect.append(
                        pyxel.pget(self.mv_boulders[boulder_id]["x"] - 1,
                                   self.mv_boulders[boulder_id]["y"] + i))
                if 13 in collision_detect:
                    return True
                self.mv_boulders[boulder_id] = {
                    "x": self.mv_boulders[boulder_id]["x"] - 1,
                    "y": self.mv_boulders[boulder_id]["y"]
                    }
                return False

        if self.direction == "right":
            if color_bar != [13, 13, 13, 13, 13, 13, 13]:
                collision_detect = []
                for i in range(0, 7):
                    collision_detect.append(
                        pyxel.pget(self.mv_boulders[boulder_id]["x"] + 8,
                                   self.mv_boulders[boulder_id]["y"] + i))
                if 13 in collision_detect:
                    return True
                self.mv_boulders[boulder_id] = {
                    "x": self.mv_boulders[boulder_id]["x"] + 1,
                    "y": self.mv_boulders[boulder_id]["y"]
                    }
                return False

        return True

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
                return self.detect_movable_boulder(west_color_bar)
            else:
                return False
        if self.direction == "right":
            if border_color in east_color_bar:
                return self.detect_movable_boulder(east_color_bar)
            else:
                return False
        if self.direction == "up":
            if border_color in north_color_bar:
                return self.detect_movable_boulder(north_color_bar)
            else:
                return False
        if self.direction == "down":
            if border_color in south_color_bar:
                return self.detect_movable_boulder(south_color_bar)
            else:
                return False

    def draw_stone_obstacle(self, x, y):
        pyxel.blt(x, y, 0, 40, 0, 8, 8)

    def draw_movable_boulder(self, id):
        pyxel.blt(self.mv_boulders[id]["x"],
                  self.mv_boulders[id]["y"], 0, 48, 0, 8, 8, colkey=0)

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
        self.draw_movable_boulder(0)
        self.draw_movable_boulder(1)
        self.draw_movable_boulder(2)
        self.draw_movable_boulder(3)
        self.draw_movable_boulder(4)
        self.draw_movable_boulder(5)
        self.draw_movable_boulder(6)
        self.draw_movable_boulder(7)


App()
