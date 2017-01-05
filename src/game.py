import itertools

FULL_BLOCK = unichr(0x2588)
FULL_BLOCK_STR = '#'
BLANK_SPACE = u' '
BLANK_SPACE_STR = ' '

#note, we're passing around x, y values, but indexing y, x

class GameOfLife(object):

    neighbor_locations = [
        (-1,-1), ( 0,-1), ( 1,-1),
        (-1, 0),          ( 1, 0),
        (-1, 1), ( 0, 1), ( 1, 1)
        ]

    def __init__(self, state):
        self.state = state
        self.height = len(self.state)
        self.width = len(self.state[0])

    def __str__(self):
        return '\n'.join(''.join([FULL_BLOCK_STR if val else BLANK_SPACE_STR
                        for val in line]) for line in self.state)

    def __unicode__(self):
        return u'\n'.join(u''.join([FULL_BLOCK if val else BLANK_SPACE
                        for val in line]) for line in self.state)

    def locations(self):
        return itertools.product(range(self.height), range(self.width))

    def tick(self):
        newstate = [[0]*self.width for _i in range(self.height)]

        for (x,y) in self.locations():
            newstate[y][x] = 1 if self.lives((x,y)) else 0

        self.state = newstate

    def neighbors(self, location):
        retval = []
        (x, y) = location
        for (dx, dy) in self.neighbor_locations:
            nextx = dx + x
            nexty = dy + y
            if nextx < 0:
                continue
            if nextx >= self.width:
                continue
            if nexty < 0:
                continue
            if nexty >= self.height:
                continue
            retval.append((nextx, nexty))
        return retval

    def lives(self, (curx, cury)):
        neighbors = self.neighbors((curx, cury))
        alive = self.state[cury][curx]
        neighbors_alive = sum(self.state[y][x] for (x,y) in neighbors)
        if alive and neighbors_alive < 2:
            return False
        if alive and neighbors_alive > 3:
            return False
        if not alive and neighbors_alive == 3:
            return True
        assert not alive or neighbors_alive in (2,3)
        return alive


if __name__ == '__main__':
    gol = GameOfLife([[1,1,0],
              [0,0,1],
              [1,1,0]])
    print unicode(gol)
    print
    gol.tick()
    print unicode(gol)
    print
    gol.tick()
    print unicode(gol)
    print
    gol.tick()
    print unicode(gol)