from game.utils import offset_cell


class Universe:
    def __init__(self, gen: list):
        self.gen = gen or list()
    
    def tick(self) -> list:
        map = {}

        for cell in self.gen:
            map.setdefault(cell, Neighboor()).set_alive()
            for step in [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]:
                adj_cell = offset_cell(cell, step)
                map.setdefault(adj_cell, Neighboor()).increment()

        nextgen = [
            cell for cell, neighboor in map.items()
            if neighboor.should_live()
        ]
        self.gen = nextgen
        return nextgen


class Neighboor:
    def __init__(self):
        self.count = 0
        self.alive = False
    
    def increment(self):
        self.count += 1
    
    def set_alive(self):
        self.alive = True

    def should_live(self):
        return (self.alive and self.count == 2) or self.count == 3
