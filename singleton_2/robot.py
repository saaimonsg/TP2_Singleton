def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Robot:
    def __init__(self, head, body, legs, feet):
        self.head = head
        self.body = body
        self.legs = legs
        self.feet = feet

# robot1 = Robot("head1","body1","legs1","feet1")
# robot2 = Robot("head2","body2","legs2","feet2")
# print(robot1)
# print(robot2)
# print(robot1.head)
# print(robot2.head)
# robot1.head = "head2"
# print(robot1.head)
# print(robot2.head)
