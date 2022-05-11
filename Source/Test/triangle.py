import os
import sys

dir = os.path.dirname(os.path.abspath("main.py"))

from ..Graphics.Runtime.render_object import RenderData, RenderShader, RenderObject

class Triangle:
    def __init__(self):
        print(dir)
        self.vertices = (
            -1, -1, 0,
            0, 0, 0,
            1, -1, 0
        )
        data = RenderData(self.vertices, 3)
        shader = RenderShader(dir + "\External\Shaders\object_v.glsl", dir + "\\External\Shaders\object_f.glsl")
        self.render_object = RenderObject()
        self.render_object.upload_data(data)
        self.render_object.upload_shader(shader)

    def prepare(self):
        self.render_object.prepare()

    def render(self):
        self.render_object.render()

    def end(self):
        self.render_object.destroy()