import yaml
import glob
import os


def load_yaml(scene):
    with open(scene, 'r') as f:
        data = yaml.safe_load(f)
    return data


def get_all_from_key(top_level_key):
    scenes = glob.glob("scenes/*.yaml")
    all_scenes = dict()
    for scene in scenes:
        formatted_scene = os.path.basename(scene).replace('.yaml', '')
        if formatted_scene != "a1":
            try:
                all_scenes[formatted_scene] = load_yaml(
                    scene).get(top_level_key, [])
            except AttributeError:
                all_scenes[formatted_scene] = {"default": ""}
    return all_scenes


def all_boulders():
    return get_all_from_key('mv_boulders')


def all_monsters():
    return get_all_from_key('monsters')
