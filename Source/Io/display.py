from unittest import runner
import pygame as pg

class Display:
    def __init__(self, width, height, title):
        self.running = True
        self.width = width
        self.height = height
        self.title = title
        pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)
        self.loop()

    def loop(self):
        while(self.running):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False


        self.quit()

    def quit(self):
        print("the raft is sinking")
        pg.quit()