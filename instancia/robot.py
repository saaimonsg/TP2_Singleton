class Robot():
    
    def __init__(self,head,body,legs,feet):
        self.__head = head
        self.__body = body
        self.__legs = legs
        self.__feet = feet
    
    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head (self,head):
        if(head is not self.__head):
            self.__head = head
    
    @property
    def body(self):
        return self.__body
    
    @body.setter
    def body (self,body):
        if(body is not self.__body):
            self.__body = body
    
    @property
    def legs(self):
        return self.__legs
    
    @legs.setter
    def legs (self,legs):
        if(legs is not self.__legs):
            self.__legs = legs
    
    @property
    def feet(self):
        return self.__feet
    
    @feet.setter
    def feet (self,feet):
        if(feet is not self.__feet):
            self.__feet = feet