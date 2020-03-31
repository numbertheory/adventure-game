import yaml


def load_yaml(scene):
    with open("scenes/{}.yaml".format(scene), 'r') as f:
        data = yaml.safe_load(f)
    return data


def position(scene):
    try:
        return load_yaml(scene).get('position', {"x": 50, "y": 50})
    except AttributeError:
        return {"x": 50, "y": 50}


def direction(scene):
    try:
        return load_yaml(scene).get('direction', "left")
    except AttributeError:
        return "left"


def mv_boulders(scene):
    try:
        return load_yaml(scene).get('mv_boulders', [])
    except AttributeError:
        return []


def walls(scene):
    try:
        return load_yaml(scene).get('walls', [])
    except AttributeError:
        return []


def scene_texts(scene):
    try:
        return load_yaml(scene).get('texts', [])
    except AttributeError:
        return []


def doors(scene):
    try:
        return load_yaml(scene).get('door_info', [])
    except AttributeError:
        return []


def ground(scene):
    try:
        return load_yaml(scene).get('ground', None)
    except AttributeError:
        return None
