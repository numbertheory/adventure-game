import pyxel
import sys
from util.collision import collision_detect, detect_door
import util.draw as draw
import util.load_scene as scene


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.scene_name = "start"
        self.scene_setup = False
        self.from_door = False
        self.initialize_scene()
        pyxel.run(self.update, self.draw_scene)

    def log_handler(self, text):
        sys.stdout.write("\r {}".format(str(text)))
        sys.stdout.flush()

    def initialize_scene(self):
        if not self.from_door:
            self.position = scene.position(self.scene_name)
        self.direction = scene.direction(self.scene_name)
        self.mv_boulders = scene.mv_boulders(self.scene_name)
        self.scene_texts = scene.scene_texts(self.scene_name)
        self.doors = scene.doors(self.scene_name)
        self.from_door = False
        self.scene_setup = True

    def update(self):
        # These controls do not work outside of this main App class.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_K):
            self.scene_name = "stage_two"
            self.scene_setup = False
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=1, period=1):
            self.direction = "right"
            door_is_there, door_info = detect_door(
                pyxel, self.position, self.direction, self.doors)
            if door_is_there:
                self.scene_name = self.doors[door_info]["gate"]["scene_name"]
                self.position = {"x": self.doors[door_info]["gate"]["x"],
                                 "y": self.doors[door_info]["gate"]["y"]}
                self.from_door = True
                self.scene_setup = False
                return None
            if not collision_detect(pyxel, self.position,
                                    self.direction, self.mv_boulders):
                self.position["x"] += 1
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, period=1):
            self.direction = "left"
            door_is_there, door_info = detect_door(
                pyxel, self.position, self.direction, self.doors)
            if door_is_there:
                self.scene_name = self.doors[door_info]["gate"]["scene_name"]
                self.position = {"x": self.doors[door_info]["gate"]["x"],
                                 "y": self.doors[door_info]["gate"]["y"]}
                self.from_door = True
                self.scene_setup = False
                return None
            if not collision_detect(pyxel, self.position,
                                    self.direction, self.mv_boulders):
                self.position["x"] -= 1
        if pyxel.btnp(pyxel.KEY_UP, hold=1, period=1):
            self.direction = "up"
            door_is_there, door_info = detect_door(
                pyxel, self.position, self.direction, self.doors)
            if door_is_there:
                self.scene_name = self.doors[door_info]["gate"]["scene_name"]
                self.position = {"x": self.doors[door_info]["gate"]["x"],
                                 "y": self.doors[door_info]["gate"]["y"]}
                self.from_door = True
                self.scene_setup = False
                return None
            if not collision_detect(pyxel, self.position,
                                    self.direction, self.mv_boulders):
                self.position["y"] -= 1
        if pyxel.btnp(pyxel.KEY_DOWN, hold=1, period=1):
            self.direction = "down"
            door_is_there, door_info = detect_door(
                pyxel, self.position, self.direction, self.doors)
            if door_is_there:
                self.scene_name = self.doors[door_info]["gate"]["scene_name"]
                self.position = {"x": self.doors[door_info]["gate"]["x"],
                                 "y": self.doors[door_info]["gate"]["y"]}
                self.from_door = True
                self.scene_setup = False
                return None
            if not collision_detect(pyxel, self.position,
                                    self.direction, self.mv_boulders):
                self.position["y"] += 1

    def draw_scene(self):
        pyxel.cls(0)
        if not self.scene_setup:
            self.initialize_scene()
        # Borders around the playable arena
        for i in range(0, 15):
            draw.stone_obstacle(pyxel, 0, i*8)
            draw.stone_obstacle(pyxel, 152, i*8)
        for i in range(1, 20):
            draw.stone_obstacle(pyxel, i*8, 0)
            draw.stone_obstacle(pyxel, i*8, 112)
        # Draw scene from YAML
        for i in range(0, len(self.scene_texts)):
            draw.scene_text(pyxel, self.scene_texts[i])

        for i in range(0, len(self.mv_boulders)):
            draw.movable_boulder(pyxel, i, self.mv_boulders)

        for i in range(0, len(self.doors)):
            draw.door(pyxel, self.doors[i])

        draw.main_character(pyxel, self.position, self.direction)


App()
