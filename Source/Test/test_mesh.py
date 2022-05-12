import os
import numpy as np

from Source.Utils.math import rotate, rotx, roty, rotz, scale, translate
from ..Io.files import load

dir = os.path.dirname(os.path.abspath("main.py"))

from ..Graphics.Runtime.render_object import RenderData, RenderShader, RenderObject

class TestMesh:
    def __init__(self):
        print(dir)
        self.vertices = (
            -0.5, -0.5, 1,
            -0.5, 0.5, 1,
            0.5, 0.5, 1,
            0.5, -0.5, 1
        )
        self.indices = (
            0, 1, 2,
            0, 2, 3
        )
        vertex_data = RenderData(self.vertices, 3, np.float32, "position")
        index_data = RenderData(self.indices, 1, np.uint32, "")
        var_v = load(dir + "\External\Shaders\object_v.glsl")
        var_f = load(dir + "\\External\Shaders\object_f.glsl")
        self.shader = RenderShader(var_v, var_f)

        self.render_object = RenderObject()
        self.render_object.upload_data(vertex_data)
        self.render_object.upload_data(index_data)
        self.render_object.upload_shader(self.shader)

    def prepare(self):
        self.render_object.prepare()
        self.transform = translate((0,0,0))
        self.transform = rotx(0)
        self.transform = roty(np.deg2rad(95))
        self.transform = rotz(0)
        self.transform = scale((1,1,1))


    def render(self):
        self.shader.upload_uniform("model", self.transform)
        self.render_object.render()

    def end(self):
        self.render_object.destroy()