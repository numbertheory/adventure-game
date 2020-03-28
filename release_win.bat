SET CURRENTDIR=c:\dungeon-dos-master

pyinstaller --clean --noconfirm --log-level=WARN --onefile --noconsole --name=dungeon-dos^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\libjpeg-9.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\libpng16-16.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\libpyxelcore.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\libtiff-5.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\libwebp-7.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\core\bin\win64\SDL2.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\SDL2_image.dll;pyxel/core/bin\win64^
  --add-data=%PYTHONPATH%\pyxel\core\bin\win64\zlib1.dll;pyxel/core/bin\win64^
  --add-data=%CURRENTDIR%\assets\image_map.pyxres;assets^
  --add-data=%CURRENTDIR%\assets\pyxel_logo_38x16.png;assets^
  --add-data=%CURRENTDIR%\util\__init__.py;util^
  --add-data=%CURRENTDIR%\util\collision.py;util^
  --add-data=%CURRENTDIR%\util\draw.py;util^
  --add-data=%CURRENTDIR%\util\load_scene.py;util^
  --add-data=%CURRENTDIR%\util\movable.py;util^
  game.py

mkdir dist/scenes

robocopy scenes dist/scenes /E