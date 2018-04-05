

def decorator_function(original_function):
    #message = msg
    def wrapper_function(*args, **kwargs):
        print('INSIDE WRAPPER')
        return original_function(*args, **kwargs)
    #return inner_function()
    return wrapper_function
    
@decorator_function
def display():
    print('PRINTING.......')

@decorator_function
def display_info(name, age):
    print('Display info {} {}'.format(name, age))
    
#decorated_display = decorator_function(display)
#decorated_display()

display()

display_info('John', 25)

 class decorator_Class(object):
 
    def __init__(self, original_function):
        self.original_function = original_function
 
    def __call))(self, *args, **kwargs):
        print('Call method executed')
        return self.original_function(*args, **kwargs)