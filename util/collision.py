from util.movable import detect_movable_boulder, closest_point


def detect_door(pyxel, position, direction, door_info):
    # Detect doors to trigger movement to new stage
    # Don't put two doors next to each other, they should be next to walls
    north, south, east, west = get_character_bubble(pyxel, position)
    if direction == "up":
        if (
                north == [9, 9, 4, 4, 9, 9] or
                north == [9, 4, 4, 9, 9, 9] or
                north == [9, 9, 9, 4, 4, 9]
        ):
            door_coords = [(x["x"], x["y"]) for x in door_info]
            character_coords = (position["x"], position["y"])
            return True, closest_point(character_coords, door_coords)
    if direction == "down":
        if (
                south == [9, 9, 4, 4, 9, 9] or
                south == [9, 4, 4, 9, 9, 9] or
                south == [9, 9, 9, 4, 4, 9]
        ):
            door_coords = [(x["x"], x["y"]) for x in door_info]
            character_coords = (position["x"], position["y"])
            return True, closest_point(character_coords, door_coords)
    if direction == "left":
        if (
                west == [9, 9, 9, 4, 4, 9, 9] or
                west == [9, 9, 4, 4, 9, 9, 9]
        ):
            door_coords = [(x["x"], x["y"]) for x in door_info]
            character_coords = (position["x"], position["y"])
            return True, closest_point(character_coords, door_coords)
    if direction == "right":
        if (
                east == [9, 9, 9, 4, 4, 9, 9] or
                east == [9, 9, 4, 4, 9, 9, 9]
        ):
            door_coords = [(x["x"], x["y"]) for x in door_info]
            character_coords = (position["x"], position["y"])
            return True, closest_point(character_coords, door_coords)
    return False, False


def get_character_bubble(pyxel, position):
    north = []
    south = []
    east = []
    west = []
    for i in range(0, 6):
        north.append(
            pyxel.pget(position["x"] + i, position["y"] - 1)
            )
        south.append(
            pyxel.pget(position["x"] + i, position["y"] + 7)
        )
    for i in range(0, 7):
        east.append(
            pyxel.pget(position["x"] + 6, position["y"] + i)
        )
        west.append(
            pyxel.pget(position["x"] - 1, position["y"] + i)
        )
    return [north, south, east, west]


def get_character_pixels(pyxel, position):
    character_points = []
    for i in range(0, 6):
        for j in range(0, 7):
            character_points.append([position["x"] + i, position["y"] + j])
    return character_points


def collision_detect(pyxel, position, direction, mv_boulders):
    # Detect collisions with borders and walls
    border_color = 13
    north, south, east, west = get_character_bubble(pyxel, position)

    if direction == "left":
        if border_color in west:
            boulder_exists = detect_movable_boulder(
                                pyxel, west, direction,
                                position, mv_boulders)
            if boulder_exists:
                return True
            else:
                bubble = get_character_bubble(pyxel, position)[3]
                if 13 in bubble:
                    return True
        else:
            return False
    if direction == "right":
        if border_color in east:
            boulder_exists = detect_movable_boulder(
                                pyxel, east, direction,
                                position, mv_boulders)
            if boulder_exists:
                return True
            else:
                bubble = get_character_bubble(pyxel, position)[2]
                if 13 in bubble:
                    return True
        else:
            return False
    if direction == "up":
        if border_color in north:
            boulder_exists = detect_movable_boulder(
                                    pyxel, north, direction,
                                    position, mv_boulders)
            if boulder_exists:
                return True
            else:
                bubble = get_character_bubble(pyxel, position)[0]
                if 13 in bubble:
                    return True
        else:
            return False
    if direction == "down":
        if border_color in south:
            boulder_exists = detect_movable_boulder(
                                pyxel, south, direction,
                                position, mv_boulders)
            if boulder_exists:
                return True
            else:
                bubble = get_character_bubble(pyxel, position)[1]
                if 13 in bubble:
                    return True
        else:
            return False


def get_tile_bubble(pyxel, position):
    north = []
    south = []
    east = []
    west = []
    for i in range(1, 9):
        north.append(
            pyxel.pget(position["x"] + i, position["y"] - 1)
            )
        south.append(
            pyxel.pget(position["x"] + i, position["y"] + 8)
        )
    for i in range(1, 9):
        east.append(
            pyxel.pget(position["x"] + 9, position["y"] + i)
        )
        west.append(
            pyxel.pget(position["x"] - 1, position["y"] + i)
        )
    return [north, south, east, west]


def get_fireball_bubble(pyxel, position):
    north = []
    south = []
    east = []
    west = []
    for i in range(1, 9):
        north.append(
            pyxel.pget(position["x"] + i, position["y"] - 1)
            )
        south.append(
            pyxel.pget(position["x"] + i, position["y"] + 8)
        )
    for i in range(1, 9):
        east.append(
            pyxel.pget(position["x"] + 8, position["y"] + i)
        )
        west.append(
            pyxel.pget(position["x"] - 1, position["y"] + i)
        )
    return [north, south, east, west]
