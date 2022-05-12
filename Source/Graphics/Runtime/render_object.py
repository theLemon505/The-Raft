from array import array
import ctypes
import numpy as np
import glfw
from sys import getsizeof
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class RenderShader:
    def __init__(self, vertex_path, fragment_path):
        with open(vertex_path, "r") as f:
            self.vertex_src = f.readlines()
        
        with open(fragment_path, "r") as f:
            self.fragment_src = f.readlines()

        print(self.vertex_src)

        self.program = compileProgram(
            compileShader(self.vertex_src, GL_VERTEX_SHADER),
            compileShader(self.fragment_src, GL_FRAGMENT_SHADER)
        )

class RenderData:
    def __init__(self, data_array, size, type, shader_ref):
        self.size = size
        self.data_array = np.array(data_array, type)
        self.data_count = len(data_array) / size
        self.shader_ref = shader_ref

class RenderObject:
    def __init__(self):
        self.vao = glGenVertexArrays(1)
        self.vbos = {}
        self.attribs = 0
        glBindVertexArray(self.vao)  
    
    def upload_data(self, data: RenderData):
        if self.attribs == 1:
            vbo = glGenBuffers(1)
            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, data.data_array.nbytes, data.data_array, GL_STATIC_DRAW)
            self.vbos[self.attribs] = data
            self.attribs += 1
        else:
            vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vbo)
            glBufferData(GL_ARRAY_BUFFER, data.data_array.nbytes, data.data_array, GL_STATIC_DRAW)
            self.vbos[self.attribs] = data
            self.attribs += 1

    def upload_shader(self, shader: RenderShader):
        self.shader = shader

    def prepare(self):
        glUseProgram(self.shader.program)

    def render(self):
        glBindVertexArray(self.vao)
        for attrib in range(self.attribs):
            if self.vbos[attrib].shader_ref != "":
                att = glGetAttribLocation(self.shader.program, self.vbos[attrib].shader_ref)
                glEnableVertexAttribArray(att)
                glVertexAttribPointer(att, self.vbos[attrib].size, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader.program)
        glDrawElements(GL_TRIANGLES, int(self.vbos[1].data_count), GL_UNSIGNED_INT, None)

        for attrib in range(self.attribs):
            if self.vbos[attrib].shader_ref != "":
                att = glGetAttribLocation(self.shader.program, self.vbos[attrib].shader_ref)
                glDisableVertexAttribArray(att)
        glBindVertexArray(0)

    def destroy(self):
        glDeleteProgram(self.shader.program)
        for vbo in self.vbos:
            glDeleteBuffers(1, vbo)