
robot = None

def setRobot(data):
    robot = data

def getRobot():
    return robot

class Robot ():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name