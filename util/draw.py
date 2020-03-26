
def stone_obstacle(pyxel, x, y):
    pyxel.blt(x, y, 0, 40, 0, 8, 8)


def movable_boulder(pyxel, id, mv_boulders):
    pyxel.blt(mv_boulders[id]["x"],
              mv_boulders[id]["y"], 0, 48, 0, 8, 8, colkey=0)


def main_character(pyxel, position, direction):
    sprite = {"left": 9, "right": 17,
              "up": 33, "down": 25}

    pyxel.blt(position["x"],
              position["y"], 0,
              sprite[direction], 0, 6, 7, colkey=1)


def scene_text(pyxel, scene_text):
    pyxel.text(scene_text["x"],
               scene_text["y"],
               scene_text["text"],
               scene_text["color"])


def door(pyxel, door_info):
    if door_info["door_type"] == "north":
        door_type = 56
    if door_info["door_type"] == "south":
        door_type = 64
    if door_info["door_type"] == "east":
        door_type = 80
    if door_info["door_type"] == "west":
        door_type = 72
    pyxel.blt(door_info["x"],
              door_info["y"],
              0, door_type, 0, 8, 8)
