'''

this is mostly an afterthought, but doesn't take too terribly much to implement, so :shrug:

'''

import game
from game import getGlider
from gamegraphics import GameGraphWin
from graphics import Point, Rectangle
import graphics


class GameGui(object):
    def __init__(self, game=None, paused=True, xscale=14, yscale=14):
        if not game:
            game = getGlider()
        self.game = game
        self.paused = paused
        self.xscale = xscale
        self.yscale = yscale

        self.game_height = self.game.height
        self.game_width = self.game.width



    def _init_graphics(self):
        #TODO: fix layering violation, kinda meh, we're still in init, mostly refactoring
        width = self.game.width * self.xscale
        height = self.game.height * self.yscale
        self.win = GameGraphWin(width=width, height=height, autoflush=False)
        self.rects = []
        for y in range(self.game_width):
            line = []
            for x in range(self.game_width):
                rect = Rectangle(Point(x*self.xscale,y*self.yscale),
                                 Point((x+1)*self.xscale, (y+1)*self.yscale))
                rect.setWidth(2)
                rect.setOutline('grey')
                rect.draw(self.win)
                line.append(rect)
            self.rects.append(line)
        self.update_fills()

    def start(self):
        self._init_graphics()
        graphics._root.after(100, self.loop)

    def loop(self):
        #always clear both, right takes precedence
        left_mouse = self.win.checkMouse()
        check_key = self.win.checkKey() == 'k'
        update = False
        if check_key:
            self.paused = not self.paused
            update = True
        elif left_mouse:
            if self.paused:
                x = int(left_mouse.x / self.xscale)
                y = int(left_mouse.y / self.yscale)
                current = self.game.get_location((x,y))
                to_set = 0 if current else 1
                self.game.set_location((x,y), to_set)
                update = True
        if not self.paused:
            self.game.tick()
            update = True
        if update:
            self.update_fills()
            graphics.update()
        graphics._root.after(100, self.loop)

    def update_fills(self):
        for y in range(self.game_width):
            for x in range(self.game_width):
                fill = None
                if self.game.get_location((x,y)):
                    fill = 'black'
                else:
                    if self.paused:
                        fill = 'red'
                    else:
                        fill = 'white'
                self.rects[y][x].setFill(fill)

# def main():
#
#     # initialize game
#     # gui game object
#     # paused to start
#     # master.after(update loop)
#         # check right mouse to know if starting / stopping
#         # check left mouse to clear, and if already stopped (and not starting):
#         # then toggle the correct box
#         #
#         # if starting: turn 0's white, update
#         # if stopping: turn 0's red, update
#         # if updating: turn that one object the correct color, update
#         # if running: tick game, update all
#         #simplified version: just update them all, don't worry about tracking each, there aren't enough to care at this point
#         # loop
#
#     #stop: turn all 0's red
#     #start: turn all 0's white
#     pass


if __name__ == '__main__':
    gg = GameGui()
    gg.start()
    _root = graphics._root
    _root.mainloop()

