def func_arg(farg, *args):
    print("form arg:",farg)
    for arg in args:
        print ("another arg:", arg)


def func_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    print(kwargs)
    print(*kwargs)
    for key in kwargs:
        print(key,kwargs[key])
        ## print ("keyword arg: %s: %s" % (key, kwargs[key]))
func_kwargs(1 , name=1,name2=3)
def bar(x,y,z):
    return x*y*z

d = {'x': 1, 'y': 3,'z':4}
print(bar(**d))