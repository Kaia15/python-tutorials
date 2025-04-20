"""
1. Function Definition:
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
            -- Positional only

2. Guidance:
    - Use positional-only if you want the name of the parameters to not be available to the user. 
    This is useful when parameter names have no real meaning, if you want to enforce the order of 
    the arguments when the function is called or if you need to take some positional parameters 
    and arbitrary keywords.

    - Use keyword-only when names have meaning and the function definition is more understandable 
    by being explicit with names or you want to prevent users relying on the position of the 
    argument being passed.

    - For an API, use positional-only to prevent breaking API changes if the parameter's name is 
    modified in the future.

"""

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def concat(*args, sep="/"):
    return sep.join(args)

def normFunc():
    
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    # Output:
    # -- Do you have any Limburger ?
    # -- I'm sorry, we're all out of Limburger
    # It's very runny, sir.
    # It's really very, VERY runny, sir.
    # ----------------------------------------
    # shopkeeper : Michael Palin
    # client : John Cleese
    # sketch : Cheese Shop Sketch

    print(concat("earth", "mars", "venus"))
    print(concat("earth", "mars", "venus", sep="."))
    # Output:
    # 'earth/mars/venus'
    # 'earth.mars.venus'

"""
3. `Lambda` Function:
    This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever 
    function objects are required. They are syntactically restricted to a single expression. Semantically, they 
    are just syntactic sugar for a normal function definition.
"""

def make_incrementor(n):
    return lambda x: x + n

def lambdaFunc():

    f = make_incrementor(42)
    f(0)
    # Output: 42

    f(1)
    # Output: 43

"""
4. Use of Annotations:
    - By passing paramters with declared types, paramter annotations are defined by a colon after the parameter name, 
    followed by an exp evaluating to the value of the annotation.
    - Return annotations are defined by a literal ->, followed by an expression,  between the parameter list and the 
    colon denoting the end of the def statement.
"""
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

def annotatedFunc():
    print(f('spam'))