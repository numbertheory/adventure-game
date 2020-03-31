import yaml


def load_yaml(scene):
    with open("scenes/{}.yaml".format(scene), 'r') as f:
        data = yaml.safe_load(f)
    return data


def position(scene):
    return load_yaml(scene).get('position', {"x": 50, "y": 50})


def direction(scene):
    return load_yaml(scene).get('direction', "left")


def mv_boulders(scene):
    return load_yaml(scene).get('mv_boulders', [])


def walls(scene):
    return load_yaml(scene).get('walls', [])


def scene_texts(scene):
    return load_yaml(scene).get('texts', [])


def doors(scene):
    return load_yaml(scene).get('door_info', [])


def ground(scene):
    return load_yaml(scene).get('ground', None)
