import time

# Intercative coding exercise
def delay_decorator(func):
    def wrapper_function():
        print("Output will be delayed for 5 seconds")
        time.sleep(5)
        func()
    return wrapper_function


@delay_decorator
def display_hello_world():
    print("Hello World")


@delay_decorator
def display_goodbye_world():
    print("Goodbye World")


# Interactive coding exercise
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = current_time
        function()
        end_time = time.time()
        print(
            f"Time taken to execute {function.__name__} is {end_time - start_time}")
        return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

# fast_function()
# slow_function()

# Interactive coding exercise


class User:
    def __init__(self, name):
        self.username = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
            print(f"Welcome {args[0].username}")
        else:
            print("User is not logged in, Sign Up and Log in here!")
    return wrapper_function


@is_authenticated_decorator
def create_blog_post(user):
    print(f"Creating a blog post for {user.username}")


user = User("Ajibade")
create_blog_post(user)
user.is_logged_in = True
create_blog_post(user)


# Advanced Decorators
# Instructions
# Create a logging_decorator() which is going to log the name of the function that was called,
#  the arguments it was given and finally the returned output.

# Expected Output
# https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd

# HINT 1: You can use function.__name__ to get the name of the function.

# HINT 2: You'll need to use *args

def loggin_decorator(function): 
    def wrapper_function(*args):
        print(f"You called {function.__name__} {args}")
        print(f"It returned: {function(*args)}")
    return wrapper_function

@loggin_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)