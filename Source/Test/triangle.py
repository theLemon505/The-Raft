import os
import numpy as np

dir = os.path.dirname(os.path.abspath("main.py"))

from ..Graphics.Runtime.render_object import RenderData, RenderShader, RenderObject

class Triangle:
    def __init__(self):
        print(dir)
        self.vertices = (
            -1, -1, 0,
            1, -1, 0,
            -1, 1, 0,
            1, 1, 0
        )
        self.indices = (
            0, 1, 2,
            1, 2, 3
        )
        vertex_data = RenderData(self.vertices, 3, np.float32)
        index_data = RenderData(self.indices, 3, np.uint32)
        shader = RenderShader(dir + "\External\Shaders\object_v.glsl", dir + "\\External\Shaders\object_f.glsl")
        self.render_object = RenderObject()
        self.render_object.upload_data(vertex_data)
        self.render_object.upload_data(index_data)
        self.render_object.upload_shader(shader)

    def prepare(self):
        self.render_object.prepare()

    def render(self):
        self.render_object.render()

    def end(self):
        self.render_object.destroy()