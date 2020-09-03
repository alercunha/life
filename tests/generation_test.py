import collections
import unittest

from game import Universe, life
from game.utils import offset_gen


class GenerationTests(unittest.TestCase):
    def test_still_lifes(self):
        for gen in [life.block(), life.bee_hive(), life.loaf(), life.boat(), life.tub()]:
            universe = Universe(gen)
            nextgen = universe.tick()
            self.assertCountEqual(gen, nextgen)

    def test_blinker(self):
        init = life.blinker()
        universe = Universe(init)
        universe.tick()
        self.assertCountEqual(universe.gen, [(1, 2), (2, 2), (3, 2)])
        universe.tick()
        self.assertCountEqual(universe.gen, init)

    def test_oscillators(self):
        oscillators = [
            (life.blinker(), 2),
            (life.toad(), 2),
            (life.beacon(), 2),
            (life.penta_decathlon(), 15),
        ]
        for init, period in oscillators:
            universe = Universe(init)
            for i in range(period - 1):
                universe.tick()
                # make sure the generation is changing in all ticks except the very last one in the period                
                self.assertNotEqual(collections.Counter(universe.gen), collections.Counter(init))
            
            universe.tick()
            self.assertCountEqual(universe.gen, init)

    def test_glider(self):
        init= life.glider()
        universe = Universe(init)
        universe.tick()
        universe.tick()
        universe.tick()
        universe.tick()
        self.assertCountEqual(offset_gen(universe.gen, (-1, -1)), init)
