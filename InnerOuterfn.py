

def outer_function(msg):
    #message = msg
    def inner_function():
        print(msg)
    #return inner_function()
    return inner_function
    
myfunc = outer_function('hi')

myfunc()
myfunc()

myfunc = outer_function('bye')
myfunc()
myfunc()