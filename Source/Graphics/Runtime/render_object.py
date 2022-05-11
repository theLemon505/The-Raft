from array import array
import ctypes
import numpy as np
import pygame as pg
from sys import getsizeof
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class RenderShader:
    def __init__(self, vertex_path, fragment_path):
        with open(vertex_path, "r") as f:
            self.vertex_src = f.readlines()
        
        with open(fragment_path, "r") as f:
            self.fragment_src = f.readlines()

        self.program = compileProgram(
            compileShader(self.vertex_src, GL_VERTEX_SHADER),
            compileShader(self.fragment_src, GL_FRAGMENT_SHADER)
        )

class RenderData:
    def __init__(self, data_array, size):
        self.size = size
        self.data_array = data_array
        self.data_count = len(data_array) / size

class RenderObject:
    def __init__(self):
        self.vao = glGenVertexArrays(1)
        self.vbos = {}
        self.attribs = 0
        glBindVertexArray(self.vao)
    
    def upload_data(self, data: RenderData):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        array_buffer = (ctypes.c_float*len(data.data_array))(*data.data_array)
        glBufferData(GL_ARRAY_BUFFER, len(data.data_array) * 4, array_buffer, GL_STATIC_DRAW)
        self.vbos[self.attribs] = data
        self.attribs += 1

    def upload_shader(self, shader: RenderShader):
        self.shader = shader

    def prepare(self):
        glUseProgram(self.shader.program)

    def render(self):
        for attrib in range(self.attribs):
            glEnableVertexAttribArray(attrib)
            glVertexAttribPointer(attrib, self.vbos[attrib].size, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader.program)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, int(self.vbos[0].data_count))
        glBindVertexArray(0)

        for attrib in range(self.attribs):
            glDisableVertexAttribArray(attrib)

        pg.display.flip()

    def destroy(self):
        for vbo in self.vbos:
            glDeleteBuffers(1, vbo)