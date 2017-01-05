'''

this file is mostly to add some right click sugar

'''

import graphics



class GameGraphWin(graphics.GraphWin):
    def __init__(self, title="Graphics Window",
                 width=200, height=200, autoflush=True):
        super(self, GameGraphWin).__init__(title, width, height, autoflush)
        self.rightMouseX = None
        self.rightMouseY = None
        self.bind("<Button-2>", self._onRighClick)
        self._rightMouseCallback = None

    def _onRightClick(self, e):
        self.rightMouseX = e.x
        self.rightMouseY = e.y
        if self._rightMouseCallback:
            self._rightMouseCallback(graphics.Point(e.x, e.y))

    def checkRightMouse(self):
        """Return last mouse click or None if right mouse has
        not been clicked since last call"""
        if self.isClosed():
            raise graphics.GraphicsError("checkRightMouse in closed window")
        self.update()
        if self.rightMouseX != None and self.rightMouseY != None:
            x,y = self.toWorld(self.rightMouseX, self.rightMouseY)
            self.rightMouseX = None
            self.rightMouseY = None
            return graphics.Point(x,y)
        else:
            return None