#!/usr/bin/env bash

# Util and scenes directories must be added to this command for release

pyinstaller --clean --noconfirm --log-level=WARN --onefile --noconsole --name=dungeon-dos \
--add-data=$VIRTUAL_ENV/lib/python3.7/site-packages/pyxel/core/bin/macos/libpyxelcore.dylib:pyxel/core/bin/macos \
--add-data=$PWD/assets/pyxel_logo_38x16.png:assets \
--add-data=$PWD/assets/image_map.pyxres:assets \
--add-data=$PWD/util/__init__.py:util \
--add-data=$PWD/util/collision.py:util \
--add-data=$PWD/util/draw.py:util \
--add-data=$PWD/util/load_scene.py:util \
--add-data=$PWD/util/load_world.py:util \
--add-data=$PWD/util/movable.py:util \
game.py

cp -r $PWD/scenes/ dist/scenes/

mv dist/ dungeon-dos/

tag=$(git describe --tags)

zip -r dungeon-dos-$tag.zip dungeon-dos/*
