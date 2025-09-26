import math
import time 
def timer(func):
    def innner(*args):
        print('time started')
        start=time.time()
        func(*args)
        print('time ended')
        end=time.time()
        print(f'total time :{end-start}' )
    return innner

@timer
def get_factorial(n):
    print('factorial starting')
    result=math.factorial(n)
    print(f'factorial of {n} is :{result}')

get_factorial(10)
#timer()()
