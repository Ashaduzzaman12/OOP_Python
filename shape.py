class shape:
    def __init__(self,name):
        self.name=name

class rectangle(shape):
    def __init__(self, name,length,width):
        self.length=length
        self.width=width
        super().__init__(name)
    
    def area(self):
        return self.length * self.width