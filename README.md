# Dungeon DOS

A quick exploration using [Pyxel](https://github.com/kitao/pyxel/blob/master/README.md).

# Development Setup

Create a virtualenvironment with `python3.7` as the python executable. Pyxel relies on some C libraries to work, so Python 3.7 is important. Don't upgrade your root system's python, install python3.7 and then point to that executable when making the virtualenvironment.

I highly recommend using [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/), as it centralizes where virtualenvs are on your system and allows you to use simple commands to activate them.

```
mkvirtualenv --python=$(which python3.7) dungeon-dos
pip install -r requirements.txt
```

# License

This dungeon game is under [MIT license](https://opensource.org/licenses/MIT). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
