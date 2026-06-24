from robot import Robot

robot1 = Robot()
robot2 = Robot()

print(robot1)  # Output: <__main__.Robot object at 0x...>
print(robot2)
print(robot1 is robot2)  # Output: True
print(robot1.name)  # Output: Robot
print(robot2.name)  # Output: Robot
robot1.name = "Robo1"
print(robot1.name)  # Output: Robo1
print(robot2.name)  # Output: Robo1
