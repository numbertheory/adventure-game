import numpy as np


def closest_point(origin, boulder_coords):
    if len(boulder_coords) != 0:
        boulder_coords = np.asarray(boulder_coords)
        boulder_dist = np.sum((boulder_coords - origin)**2, axis=1)
        return np.argmin(boulder_dist)


def detect_movable_boulder(pyxel, color_bar, direction,
                           position, mv_boulders):
    # Decide which boulder is moving
    boulder_coords = [(x["x"], x["y"]) for x in mv_boulders]
    character_coords = (position["x"], position["y"])
    boulder_id = closest_point(character_coords, boulder_coords)
    if direction == "up":
        if (
                color_bar != [13, 13, 13, 13, 13, 13] and
                9 not in color_bar
        ):
            collision_detect = []
            for i in range(0, 6):
                collision_detect.append(
                    pyxel.pget(mv_boulders[boulder_id]["x"] + i,
                               mv_boulders[boulder_id]["y"] - 1))
            if 13 in collision_detect:
                return True
            else:
                mv_boulders[boulder_id] = {
                    "x": mv_boulders[boulder_id]["x"],
                    "y": mv_boulders[boulder_id]["y"] - 1
                    }
                return False

    if direction == "down":
        if (
                color_bar != [13, 13, 13, 13, 13, 13] and
                9 not in color_bar
        ):
            collision_detect = []
            for i in range(0, 7):
                collision_detect.append(
                    pyxel.pget(mv_boulders[boulder_id]["x"] + i,
                               mv_boulders[boulder_id]["y"] + 8))
            if 13 in collision_detect:
                return True
            mv_boulders[boulder_id] = {
                "x": mv_boulders[boulder_id]["x"],
                "y": mv_boulders[boulder_id]["y"] + 1
                }
            return False

    if direction == "left":
        if (
                color_bar != [13, 13, 13, 13, 13, 13, 13] and
                9 not in color_bar
        ):
            collision_detect = []
            for i in range(0, 7):
                collision_detect.append(
                    pyxel.pget(mv_boulders[boulder_id]["x"] - 1,
                               mv_boulders[boulder_id]["y"] + i))
            if 13 in collision_detect:
                return True
            mv_boulders[boulder_id] = {
                "x": mv_boulders[boulder_id]["x"] - 1,
                "y": mv_boulders[boulder_id]["y"]
                }
            return False

    if direction == "right":
        if (
                color_bar != [13, 13, 13, 13, 13, 13, 13] and
                9 not in color_bar
        ):
            collision_detect = []
            for i in range(0, 7):
                collision_detect.append(
                    pyxel.pget(mv_boulders[boulder_id]["x"] + 8,
                               mv_boulders[boulder_id]["y"] + i))
            if 13 in collision_detect:
                return True
            mv_boulders[boulder_id] = {
                "x": mv_boulders[boulder_id]["x"] + 1,
                "y": mv_boulders[boulder_id]["y"]
                }
            return False

    return True
