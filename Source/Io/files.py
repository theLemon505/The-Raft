import sys

def load(path):
    if sys.platform == "darwin":
        var = path.replace("\\","/")
        return var
    else:
        return path