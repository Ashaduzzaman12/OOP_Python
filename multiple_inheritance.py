class family:
    def __init__(self,address):
        self.address=address


class School :
    def __init__(self,id,level):
        self.id=id
        self.level=level

class sports:
    def __init__(self,game):
        self.game=game

class student(family,School,sports):
    def __init__(self, address,id,level,game):
        School.__init__(self,id,level)
        sports.__init__(self,game)
        family.__init__(self.address )
        super().__init__(address)