class Robot():
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,name="Robot"):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name (self,name):
        if(name is not self.__name):
            self.__name = name