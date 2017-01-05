

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
        for y in range(self.height):
            for x in range(self.width):
                yield (x,y)

    def tick(self):
        newstate = []
        for i in range(self.height):
            newstate.append([0]*self.width)

        for location in self.locations():
            newstate = self.live_or_die(self.neighbors(location))

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



if __name__ == '__main__':
    print unicode(GameOfLife([[1,1,0],
                      [0,0,1],
                      [1,1,0]]))