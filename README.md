[ClassyStache](http://tomshen.github.com/ClassyStache/)
============
_The classiest game ever_

What is ClassyStache and why should I care?
-------------------------------------------
It's Asteroids, but you are a mustache shooting noses at monocles. What more could you ask for?

Playing the game
----------------
There are two ways to run the game:
* `python main.py` -- requires [Python 2.7](http://www.python.org/download/) and [pygame](http://www.pygame.org/download.shtml)
* (On Windows) Download [ClassyStache.zip](http://dl.tomshen.me/ClassyStache.zip), extract to a location of your choice, and run `main.exe`

Technical stuff
---------------
* `settingsloader.py` - all the constants for the program gathered in one place for easy modification
* `sprites.py` - definitions for all the different sprites used in the game
* `gui.py` - methods for updating and drawing the gui
* `bigimageloader.py` - loads all images and creates rects for them, if necessary (975 by 600)
* `imageloader.py` - loads all images and creates rects for them, if necessary (650 by 400)
* `main.py` - creates and updates display, handles game logic
