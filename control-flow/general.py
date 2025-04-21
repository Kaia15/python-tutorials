"""
1. `pass` statement
""" 
def initlog(*args):
    pass   # Remember to implement this!

"""
2. `match` statement
    2.1 Like Javascript's `switch` statement
    2.2 Can be used in nested patterns arbitrarily 
    2.3 Can be used with `if` w.out `else` statement
    2.4 Can be applied in writing Enum
"""

# 2.1
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

class Point:
    # passing arguments
    __match_args__ = ('x', 'y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def matchStatement():
    points = list(input())
    point = tuple(input())

    # 2.2
    match points:
        case []:
            print ("There is no point!")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _: # other remaining cases
            print("Something else")

    # 2.3
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")

    # 2.4 
    color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")

"""
3. `return` statement
    3.1 In a function, there are 2 subcases:
        3.1.2 None: without an expression argument
        3.1.2 A value from function
"""
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


def returnStatement():
    # Now call the function we just defined:
    fib(2000)

    # 3.1.1
    f = fib
    f(100)

    # 3.1.2
    f100 = fib2(100)    # call it
    f100                # write the result

    
