class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _dist(self, point):
        return(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5)

    def _info(self):
        return(self.x, self.y)