from ...Utils.math import rotx, roty, rotz, translate, perspective

class Camera:
    def __init__(self):
        self.view_matrix = translate((0, 0, -1))
        self.view_matrix = rotx(0)
        self.view_matrix = roty(0)
        self.view_matrix = rotz(0)
        self.perspective_matrix = perspective(70, float(540)/float(400), 0.01, 1000)