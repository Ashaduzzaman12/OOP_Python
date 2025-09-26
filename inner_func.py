# function is a first class object 

def double_decker():
    print('starting the double decker')
    def  inner_fun():
        print('inside the inner')
        return 6000
    return inner_fun

print(double_decker())
print(double_decker()())


def do_something(work):
    print('work started')
    print(work)
    print('work ended')

def coding ():
    print('coding in python')

def sleeping():
    print('sleeping in peace')

do_something(coding)
 

do_something(sleeping)


