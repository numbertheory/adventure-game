

def stone_obstacle(pyxel, x, y):
    pyxel.blt(x, y, 0, 40, 0, 8, 8)


def movable_boulder(pyxel, id, mv_boulders):
    pyxel.blt(mv_boulders[id]["x"],
              mv_boulders[id]["y"], 0, 48, 0, 8, 8, colkey=0)


def wall(pyxel, id, walls):
    pyxel.blt(walls[id]["x"],
              walls[id]["y"], 0, 56, 8, 8, 8, colkey=0)


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


def fire(pyxel, frame):
    fires = [[0, 16], [8, 16], [0, 24], [8, 24]]
    pyxel.blt(20, 0,
              0, fires[frame][0], fires[frame][1], 8, 8)


def goblet(pyxel, x, y):
    pyxel.blt(x, y,
              0, 48, 8, 8, 8)


def monster(pyxel, monster_info):
    pyxel.blt(monster_info["x"],
              monster_info["y"],
              0, 0, 32, 8, 8, colkey=0)


def ground(pyxel, ground):
    playa = []
    for i in range(1, 20):
        playa.append([[i*8, 8], [i*8, 16], [i*8, 24], [i*8, 32],
                     [i*8, 40], [i*8, 48], [i*8, 56], [i*8, 64],
                     [i*8, 72], [i*8, 80], [i*8, 88], [i*8, 96],
                     [i*8, 104]])
    if ground == "tiles":
        ground_info = [[32, 8], [40, 8], [32, 16], [40, 16]]
    elif ground == "grass":
        ground_info = [[16, 8], [24, 8], [16, 16], [24, 16]]
    else:
        ground_info = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    counter = 0
    for i in range(0, 18):
        for tile in playa[i]:
            set_tile = ground_info[counter]
            if tile[1] + 8 != 112:
                pyxel.blt(tile[0], tile[1] + 8,
                          0, set_tile[0], set_tile[1], 8, 8)
            if counter == 3:
                counter = 0
            else:
                counter += 1


def start_fireball(pyxel, character_position, direction):
    if direction == "left":
        fireball_position_x = character_position["x"] - 8
        fireball_position_y = character_position["y"]
    if direction == "right":
        fireball_position_x = character_position["x"] + 8
        fireball_position_y = character_position["y"]
    if direction == "up":
        fireball_position_x = character_position["x"]
        fireball_position_y = character_position["y"] - 8
    if direction == "down":
        fireball_position_x = character_position["x"]
        fireball_position_y = character_position["y"] + 8
    pyxel.blt(fireball_position_x, fireball_position_y,
              0, 0, 8, 8, 8, colkey=0)
    return [fireball_position_x,
            fireball_position_y]


def fireball(pyxel, fireball_coords):
    if fireball_coords["animate"] == 0:
        fireball_frame = [0, 8]
        next_frame = 1
    else:
        fireball_frame = [8, 8]
        next_frame = 0
    if fireball_coords["direction"] == "left":
        fireball_position_x = fireball_coords["x"] - 1
        fireball_position_y = fireball_coords["y"]
    if fireball_coords["direction"] == "right":
        fireball_position_x = fireball_coords["x"] + 1
        fireball_position_y = fireball_coords["y"]
    if fireball_coords["direction"] == "up":
        fireball_position_x = fireball_coords["x"]
        fireball_position_y = fireball_coords["y"] - 1
    if fireball_coords["direction"] == "down":
        fireball_position_x = fireball_coords["x"]
        fireball_position_y = fireball_coords["y"] + 1
    pyxel.blt(fireball_position_x,
              fireball_position_y,
              0, fireball_frame[0], fireball_frame[1], 8, 8, colkey=0)
    return [fireball_position_x,
            fireball_position_y, next_frame]
