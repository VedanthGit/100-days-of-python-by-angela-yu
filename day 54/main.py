import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function

@delay_decorator
def hello():

    print("Hello")
    
@delay_decorator
def bye():
    print("Byee")

hello()

bye()