import pygame as pg

class Display:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)