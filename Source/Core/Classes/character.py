from argparse import Namespace
import sys
import os

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir + "/Source/Graphics/Runtime")

from ...Graphics.Runtime.render_object import RenderShader, RenderData, RenderObject

class Eye:
    pass

class Character:
    def __init__(self):
        render_shader = RenderShader(dir + "/External/Shaders/object_v.glsl", dir + "/External/Shaders/object_f.glsl")
        render_data = RenderData([], 0, 0)
        self.render_object = RenderObject()
        self.render_object.upload_data(render_data)
        self.render_object.upload_shader(render_shader)
        self.render_object.prepare()

    def loop(self):
        pass

    def render(self):
        self.render_object.render()

    def end(self):
        self.render_object.destroy()