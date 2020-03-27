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

I highly reccommend using [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/), as it centralizes where virtualenvs are on your system and allows you to use simple commands to activate them.

```
mkvirtualenv --python=$(which python3.7) dungeon-dos
pip install -r requirements.txt
```

# License

This dungeon game is under [MIT license](https://opensource.org/licenses/MIT). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
