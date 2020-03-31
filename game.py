import pyxel
import sys
import random
from util.collision import collision_detect, detect_door
from util.collision import get_character_bubble, get_character_pixels
from util.collision import get_tile_bubble, get_fireball_bubble
import util.draw as draw
import util.load_scene as scene
from util.load_world import all_boulders, all_monsters
from util.movable import detect_movable_boulder, closest_point


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Dungeon DOS")
        pyxel.load("assets/image_map.pyxres")
        self.all_boulders = all_boulders()
        self.scene_name = "a1"
        self.scene_setup = False
        self.from_door = False
        self.initialize_scene()
        self.inventory_up = False
        self.main_play = True
        self.fireballs = 10
        self.fireball_in_flight = False
        self.fireball_coords = {
            "x": 0, "y": 0, "range": 0, "direction": None, "animate": 0}
        self.coins = 5
        self.health = 10
        self.monsters = all_monsters()
        self.death = False
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
        self.ground = scene.ground(self.scene_name)
        self.doors = scene.doors(self.scene_name)
        self.walls = scene.walls(self.scene_name)
        self.from_door = False
        self.scene_setup = True

    def update(self):
        # These controls do not work outside of this main App class.
        if self.scene_name == "a1":
            boulder_key = "a1_duplicate"
        else:
            boulder_key = self.scene_name
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            self.fireballs = 10
        if pyxel.btnp(pyxel.KEY_F):
            if self.main_play and not self.fireball_in_flight:
                if self.fireballs >= 1:
                    self.fireballs -= 1
                    fire_coords = draw.start_fireball(
                                    pyxel, self.position, self.direction)
                    self.fireball_coords = {
                        "x": fire_coords[0],
                        "y": fire_coords[1],
                        "range": 100,
                        "direction": self.direction,
                        "animate": 0}
                    self.fireball_in_flight = True

        if pyxel.btnp(pyxel.KEY_I):
            if not self.inventory_up:
                self.inventory_up = True
                self.main_play = False
            else:
                self.inventory_up = False
                self.main_play = True
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=1, period=1):
            if self.main_play:
                self.direction = "right"
                door_is_there, door_info = detect_door(
                    pyxel, self.position, self.direction, self.doors)
                if door_is_there:
                    self.scene_name = self.doors[door_info]["gate"].get(
                        "scene_name")
                    self.position = {"x": self.doors[door_info]["gate"]["x"],
                                     "y": self.doors[door_info]["gate"]["y"]}
                    self.from_door = True
                    self.scene_setup = False
                    self.fireball_in_flight = False
                    return None
                if pyxel.btnp(pyxel.KEY_LEFT_SHIFT, hold=1, period=1):
                    character_bubble = get_character_bubble(
                        pyxel, self.position)
                    if (
                        13 in character_bubble[3] and
                        9 not in character_bubble[3] and
                        character_bubble[3] != [13, 13, 13, 13, 13, 13, 13]
                    ):
                        detect_movable_boulder(
                            pyxel, character_bubble[3],
                            self.direction,
                            self.position,
                            self.all_boulders[boulder_key])
                if not collision_detect(pyxel, self.position,
                                        self.direction,
                                        self.all_boulders[boulder_key]):
                    self.position["x"] += 1
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, period=1):
            if self.main_play:
                self.direction = "left"
                door_is_there, door_info = detect_door(
                    pyxel, self.position, self.direction, self.doors)
                if door_is_there:
                    self.scene_name = self.doors[door_info]["gate"].get(
                        "scene_name")
                    self.position = {"x": self.doors[door_info]["gate"]["x"],
                                     "y": self.doors[door_info]["gate"]["y"]}
                    self.from_door = True
                    self.scene_setup = False
                    self.fireball_in_flight = False
                    return None
                if pyxel.btnp(pyxel.KEY_LEFT_SHIFT, hold=1, period=1):
                    character_bubble = get_character_bubble(
                        pyxel, self.position)
                    if (
                        13 in character_bubble[2] and
                        9 not in character_bubble[2] and
                        character_bubble[2] != [13, 13, 13, 13, 13, 13, 13]
                    ):
                        detect_movable_boulder(
                            pyxel, character_bubble[2],
                            self.direction,
                            self.position,
                            self.all_boulders[boulder_key])
                if not collision_detect(pyxel, self.position,
                                        self.direction,
                                        self.all_boulders[boulder_key]):
                    self.position["x"] -= 1
        if pyxel.btnp(pyxel.KEY_UP, hold=1, period=1):
            if self.main_play:
                self.direction = "up"
                door_is_there, door_info = detect_door(
                    pyxel, self.position, self.direction, self.doors)
                if door_is_there:
                    self.scene_name = self.doors[door_info]["gate"].get(
                        "scene_name")
                    self.position = {"x": self.doors[door_info]["gate"]["x"],
                                     "y": self.doors[door_info]["gate"]["y"]}
                    self.from_door = True
                    self.scene_setup = False
                    self.fireball_in_flight = False
                    return None
                if pyxel.btnp(pyxel.KEY_LEFT_SHIFT, hold=1, period=1):
                    character_bubble = get_character_bubble(
                        pyxel, self.position)
                    if (
                        13 in character_bubble[1] and
                        9 not in character_bubble[1] and
                        character_bubble[1] != [13, 13, 13, 13, 13, 13]
                    ):
                        detect_movable_boulder(
                            pyxel, character_bubble[1],
                            self.direction,
                            self.position,
                            self.all_boulders[boulder_key])
                if not collision_detect(pyxel, self.position,
                                        self.direction,
                                        self.all_boulders[boulder_key]):
                    self.position["y"] -= 1
        if pyxel.btnp(pyxel.KEY_DOWN, hold=1, period=1):
            if self.main_play:
                self.direction = "down"
                door_is_there, door_info = detect_door(
                    pyxel, self.position, self.direction, self.doors)
                if door_is_there:
                    self.scene_name = self.doors[door_info]["gate"].get(
                        "scene_name"
                    )
                    self.position = {"x": self.doors[door_info]["gate"]["x"],
                                     "y": self.doors[door_info]["gate"]["y"]}
                    self.from_door = True
                    self.scene_setup = False
                    self.fireball_in_flight = False
                    return None
                if pyxel.btnp(pyxel.KEY_LEFT_SHIFT, hold=1, period=1):
                    character_bubble = get_character_bubble(
                        pyxel, self.position)
                    if (
                        13 in character_bubble[0] and
                        9 not in character_bubble[0] and
                        character_bubble[0] != [13, 13, 13, 13, 13, 13]
                    ):
                        detect_movable_boulder(
                            pyxel, character_bubble[0],
                            self.direction,
                            self.position,
                            self.all_boulders[boulder_key])
                if not collision_detect(pyxel, self.position,
                                        self.direction,
                                        self.all_boulders[boulder_key]):
                    self.position["y"] += 1

    def draw_scene(self):
        if self.health < 0:
            self.death = True
        if self.death:
            pyxel.cls(0)
            for i in range(1, 15):
                draw.stone_obstacle(pyxel, 0, i*8)
                draw.stone_obstacle(pyxel, 152, i*8)
            for i in range(1, 20):
                draw.stone_obstacle(pyxel, i*8, 8)
                draw.stone_obstacle(pyxel, i*8, 112)
            pyxel.text(55,
                       41,
                       "YOU DIED",
                       10)

        if self.main_play and not self.death:
            pyxel.cls(0)
            if self.scene_name == "a1":
                boulder_key = "a1_duplicate"
                monster_key = "a1_duplicate"
            else:
                boulder_key = self.scene_name
                monster_key = self.scene_name
            if not self.scene_setup:
                self.initialize_scene()
            # Borders around the playable arena
            for i in range(1, 15):
                draw.stone_obstacle(pyxel, 0, i*8)
                draw.stone_obstacle(pyxel, 152, i*8)
            for i in range(1, 20):
                draw.stone_obstacle(pyxel, i*8, 8)
                draw.stone_obstacle(pyxel, i*8, 112)

            # Draw the ground tiles

            draw.ground(pyxel, self.ground)

            # Draw fireball counter symbol
            self.fire_frame = 0
            if random.choice(range(0, 4)) == 0:
                self.fire_frame += 1
            if self.fire_frame == 4:
                self.fire_frame = 0

            draw.fire(pyxel, self.fire_frame)
            pyxel.text(29, 2, str(self.fireballs), 8)

            # Draw life meter
            draw.goblet(pyxel, 0, 0)
            pyxel.text(8, 2, str(self.health), 8)

            # move monsters
            for i in range(0, len(self.monsters[monster_key])):
                if not self.monsters[monster_key]["dead"]:
                    character_pixels = get_character_pixels(
                        pyxel, self.position)
                    monster_bubble = get_tile_bubble(
                        pyxel, self.monsters[monster_key][i])
                    if (random.choice(range(0, 6)) == 0 and
                       (13 not in monster_bubble[1])):
                        self.monsters[monster_key][i]["y"] += 1
                        monster_position = [self.monsters[monster_key][i]["x"],
                                            self.monsters[monster_key][i]["y"]]
                        if monster_position in character_pixels:
                            self.health -= 1
                    if (random.choice(range(0, 6)) == 0 and
                       (13 not in monster_bubble[2])):
                        self.monsters[monster_key][i]["x"] += 1
                        monster_position = [self.monsters[monster_key][i]["x"],
                                            self.monsters[monster_key][i]["y"]]
                        if monster_position in character_pixels:
                            self.health -= 1
                    if (random.choice(range(0, 6)) == 0 and
                       (13 not in monster_bubble[0])):
                        self.monsters[monster_key][i]["y"] -= 1
                        monster_position = [self.monsters[monster_key][i]["x"],
                                            self.monsters[monster_key][i]["y"]]
                        if monster_position in character_pixels:
                            self.health -= 1
                    if (random.choice(range(0, 6)) == 0 and
                       (13 not in monster_bubble[3])):
                        self.monsters[monster_key][i]["x"] -= 1
                        monster_position = [self.monsters[monster_key][i]["x"],
                                            self.monsters[monster_key][i]["y"]]
                        if monster_position in character_pixels:
                            self.health -= 1

            # Draw scene from YAML
            for i in range(0, len(self.scene_texts)):
                draw.scene_text(pyxel, self.scene_texts[i])

            for i in range(0, len(self.all_boulders[boulder_key])):
                draw.movable_boulder(pyxel, i, self.all_boulders[boulder_key])

            for i in range(0, len(self.walls)):
                draw.wall(pyxel, i, self.walls)

            for i in range(0, len(self.doors)):
                draw.door(pyxel, self.doors[i])

            for i in range(0, len(self.monsters[monster_key])):
                if not self.monsters[monster_key][i]["dead"]:
                    draw.monster(pyxel, self.monsters[monster_key][i])

            draw.main_character(pyxel, self.position, self.direction)

            if self.fireball_in_flight and not self.death:
                fireball_coords = draw.fireball(pyxel, self.fireball_coords)
                bubble = get_tile_bubble(pyxel, self.fireball_coords)
                fire_bubble = get_fireball_bubble(pyxel, self.fireball_coords)
                fireball_collide = False
                enemy_hit = False
                if self.fireball_coords["direction"] == "left":
                    if 13 in bubble[3]:
                        fireball_collide = True
                    if 8 in fire_bubble[3]:
                        enemy_hit = True
                if self.fireball_coords["direction"] == "right":
                    if 13 in bubble[2]:
                        fireball_collide = True
                    if 8 in fire_bubble[2]:
                        enemy_hit = True
                if self.fireball_coords["direction"] == "up":
                    if 13 in bubble[0]:
                        fireball_collide = True
                    if 8 in fire_bubble[0]:
                        enemy_hit = True
                if self.fireball_coords["direction"] == "down":
                    if 13 in bubble[1]:
                        fireball_collide = True
                    if 8 in fire_bubble[1]:
                        enemy_hit = True

                if not fireball_collide:
                    self.fireball_coords["x"] = fireball_coords[0]
                    self.fireball_coords["y"] = fireball_coords[1]
                    self.fireball_coords["range"] -= 1
                    self.fireball_coords["animate"] = fireball_coords[2]
                    if self.fireball_coords["range"] <= 0:
                        self.fireball_in_flight = False
                        self.fireball_range = 10
                else:
                    self.fireball_in_flight = False
                    self.fireball_range = 10

                monster_coords = [(x["x"], x["y"])
                                  for x in self.monsters[monster_key]]
                fb_coords = (self.fireball_coords["x"],
                             self.fireball_coords["y"])
                if enemy_hit:
                    monster_id = closest_point(fb_coords,
                                               monster_coords)
                    self.monsters[monster_key][monster_id]["dead"] = True
                    self.fireball_in_flight = False
                    self.fireball_range = 10

        if self.inventory_up and not self.death:
            pyxel.cls(0)
            for i in range(0, 15):
                draw.stone_obstacle(pyxel, 0, i*8)
                draw.stone_obstacle(pyxel, 152, i*8)
            for i in range(1, 20):
                draw.stone_obstacle(pyxel, i*8, 0)
                draw.stone_obstacle(pyxel, i*8, 112)
            draw.scene_text(pyxel, {"x": 10, "y": 10,
                                    "text": "Inventory",
                                    "color": 8})
            draw.scene_text(pyxel,
                            {"x": 10, "y": 20,
                             "text": "Fireballs: {}".format(self.fireballs),
                             "color": 6})
            draw.scene_text(pyxel,
                            {"x": 10, "y": 30,
                             "text": "Coins: {}".format(self.coins),
                             "color": 6})


App()
