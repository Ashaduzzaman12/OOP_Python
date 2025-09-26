class engine:
    def __init__(self):
        pass
    def start(self):
        return "engine started"

#car has an engine 
class car:
    def __init__(self):
        self.engine=engine()
        self.driver=driver()
    def start(self):
        self.engine.start()
    

class driver:
    def __init__(self):
        pass
