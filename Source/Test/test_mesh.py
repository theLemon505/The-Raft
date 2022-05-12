import os
import numpy as np
from ..Io.files import load

dir = os.path.dirname(os.path.abspath("main.py"))

from ..Graphics.Runtime.render_object import RenderData, RenderShader, RenderObject

class TestMesh:
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
        vertex_data = RenderData(self.vertices, 3, np.float32, "position")
        index_data = RenderData(self.indices, 3, np.uint32, "")
        var_v = load(dir + "\External\Shaders\object_v.glsl")
        var_f = load(dir + "\\External\Shaders\object_f.glsl")
        shader = RenderShader(var_v, var_f)
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