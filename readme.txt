to run

python game.py
  runs game with a 25/25 grid with glider in the center, prints each generation as spaces and blocks,
  with a counter of how many cells are alive in each generation

python tkgame.py
  runs a tkinter gui version, see below for details of how to play

ok, quick rundown of files:

 * game.py
   main business logic
     has class GameOfLife: to instantiate, pass in a list of length M full of lists of length N,
     contents int(0) for empty squares, int(1) for "alive"

     method getGlider() takes a width and a height and returns an appropriate list of lists with a glider at the center (less than 3x3 will likely break)

  * gamegraphics.py : class GameGraphWin
    intended as a way to grab right mouse button, but something doesn't quite work yet (substituted with key binding, see below)

  * graphics.py : see contents of file, used as graphics / gui library
    grabbed from http://mcsp.wartburg.edu/zelle/python/graphics.py on Jan 4, 2016

  * tkgame.py : tk interactive game of life:
    GameGui() takes a game and some other parameters to construct a gui representation of the GOL.
    to play, grab focus of the window, use the "k" key to pause/resume.
    game is paused when dead cells are red
    (colorblind folks: not sure what this shows up as, edit source and replace "red" as appropriate if not enough contrast)
    when paused, left click will toggle dead/alive cells.

caveats:
  error handling, especially exit conditions are poor/missing.
  performance is pretty poor, especially with larger grids, not sure where the bottleneck is,
  but I suspect the GUI updates to be far in excess of the actual changes happening
  (though if every cell changed each tick, this would still be a problem)
  I haven't profiled, so, not sure how bad the base GameOfLife class implementation is.

