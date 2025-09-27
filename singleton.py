#singleton->one single instance 
# if we want new instance ,we will get old one

class singleton:
    _instance=None
    def __init__(self):
        if singleton._instance is None:
            singleton._instance=self
        else:
            raise Exception('This is singleton,already have an instance,one by calling get_instance method')
        
    @staticmethod
    def get_instance():
        if singleton._instance is None:
            singleton()
        return singleton._instance