import yaml
import glob
import os


def load_yaml(scene):
    with open(scene, 'r') as f:
        data = yaml.safe_load(f)
    return data


def all_boulders():
    scenes = glob.glob("scenes/*.yaml")
    all_scenes = dict()
    for scene in scenes:
        formatted_scene = os.path.basename(scene).replace('.yaml', '')
        if formatted_scene != "start":
            all_scenes[formatted_scene] = load_yaml(
                scene).get('mv_boulders', [])
    return all_scenes
