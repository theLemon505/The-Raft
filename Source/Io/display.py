from logging import exception
from random import triangular
from sqlite3 import Time
from unittest import runner
import glfw
from OpenGL.GL import *

from Source.Test.test_mesh import TestMesh

class Display:
    def __init__(self, width, height, title):
        self.running = True
        self.width = width
        self.height = height
        self.title = title

        if not glfw.init():
            raise Exception("glfw cannot be instantiated")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.window = glfw.create_window(width, height, title, None, None)

        if not self.window:
            glfw.terminate()
            raise Exception("glfw cannot create a window")

        glfw.set_window_pos(self.window, 400, 200)

        glfw.make_context_current(self.window)

        self.init()
        self.loop()

    def init(self):
        self.tri = TestMesh()
        self.tri.prepare()

    def loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.tri.render()
            glfw.swap_buffers(self.window)

        self.quit()

    def quit(self):
        self.tri.end()
        print("the raft is sinking")
        glfw.terminate()