class CPU:
    def __init__(self,core):
        self.core=core


class RAM:
    def __init__(self,size):
        self.size=size
        
class HardDrive:
    def __init__(self,capacity):
        self.capacity=capacity


class computer:
    def __init__(self,cores,ram_size,hd_capacity):
        self.cpu=CPU(cores)
        self.ram=RAM(ram_size)
        self.hard_disc=HardDrive(hd_capacity)
        