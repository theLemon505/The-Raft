import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compilerProgram, compileShader

class RenderShader:
    def __init__(self, vertex_path, fragment_path):
        with open(vertex_path, "r") as f:
            self.vertex_src = f.readlines()
        
        with open(fragment_path, "r") as f:
            self.fragment_src = f.readlines()

        self.program = compilerProgram(
            compileShader(self.vertex_src, GL_VERTEX_SHADER),
            compileShader(self.fragment_src, GL_FRAGMENT_PATH)
        )

class RenderData:
    def __init__(self, data_array, size, data_count):
        self.size = size
        self.data_array = data_array
        self.data_count = data_count

class RenderObject:
    def __init__(self):
        self.vao = glGenVertexArrays(1)
        self.vbos = {}
        self.attribs = 0
        glBindVertexArray(self.vao)
    
    def upload_data(self, data: RenderData):
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
        for attrib in self.attribs:
            glEnableVertexAttribPointer(attrib)
            glVertexAttribPointer(attrib, self.vbos[attrib].size, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader.program)
        glBindVertexArrays(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, self.vbos[0].data_count)

        pg.display.flip()

    def destroy(self):
        for vbo in self.vbos:
            glDeleteBuffers(1, vbo)