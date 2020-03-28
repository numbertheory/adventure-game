# Dungeon DOS

A quick exploration using [Pyxel](https://github.com/kitao/pyxel/blob/master/README.md).

# Running the Binaries

On Mac and Linux, you will need to install some of the libraries that developers use in order to run the binary distributions. See below:

## Ubuntu

On Ubuntu (and other Ubuntu distros), run this command:

```
sudo apt install libsdl2-dev libsdl2-image-dev
```

## MacOS

With Homebrew, run this command:

```
brew install sdl2 sdl2_image
```


# Development Setup

Create a virtualenvironment with `python3.7` as the python executable. Pyxel relies on some C libraries to work, so Python 3.7 is important. Don't upgrade your root system's python, install python3.7 and then point to that executable when making the virtualenvironment.

I highly recommend using [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/), as it centralizes where virtualenvs are on your system and allows you to use simple commands to activate them.

```
mkvirtualenv --python=$(which python3.7) dungeon-dos
pip install -r requirements.txt
```

# Controls

+-----------------+-----------------------------+
| Arrow keys      | Move character (N, S, E, W) |
+-----------------+-----------------------------+
| Left Shift Key  | Pull nearby stone           |
+-----------------+-----------------------------+
| I               | Toggle inventory            |
+-----------------+-----------------------------+
| Escape, or `Q`  | Quit game                   |
+-----------------+-----------------------------+

Note: To pull a stone, hold down the left shift key and move
with the arrow keys which will drag the stone behind you. Not
all surfaces of the stone will accept the pull. This is an
accident of how the feature was implemented, but I like the mechanic
as pulling a huge boulder takes a bit more effort than pushing one.


# License

This dungeon game is under [MIT license](https://opensource.org/licenses/MIT). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
