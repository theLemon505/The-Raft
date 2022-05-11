from random import triangular
from unittest import runner
import pygame as pg

from Source.Test.triangle import Triangle

class Display:
    def __init__(self, width, height, title):
        self.running = True
        self.width = width
        self.height = height
        self.title = title
        pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)
        self.init()
        self.loop()

    def init(self):
        self.tri = Triangle()
        self.tri.prepare()

    def loop(self):
        while(self.running):
            self.tri.render()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        self.quit()

    def quit(self):
        self.tri.end()
        print("the raft is sinking")
        pg.quit()