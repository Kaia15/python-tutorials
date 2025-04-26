
### Simple Class Creation

#### Code 
    ```
    class Cat:
        species = "Feline"
        def meow(self):
            print ("meow!")

    my_cat = Cat()
    my_cat.name = "Whiskers"

    print(Cat.__dict__['meow'] is Cat().meow) # False
    print(Cat.__dict__['meow'] is Cat().meow.__func__) # True

    print (Cat.__mro__) # (<class '__main__.Cat'>, <class 'object'>)
    ```
- In CPython (the default Python implementation), `id(obj)` returns the **memory address** of the object (technically the address of the underlying PyObject * struct in C).
- In this example, the class attribute (or class variable) `species` is created when the class is created, not when instances of the class are created.
- Also, `Cat.meow` is **different** from `Cat().meow`, since `Cat().meow` wraps 2 more props including `__func__` and `__self__`.
    - `__func__`: the actual function of `Cat.meow`
    - `__self__`: the instance method of `Cat()`

#### Diagram
    ```
    [Stack]                             [Heap]
    -----------------                -----------------------
    | Cat       | ────────────────→ | Class object (Cat)    |
    -----------------               |-----------------------|
                                    | __name__ = 'Cat'      |
                                    | __dict__ = {          |
                                    |   'species': 'Feline' |
                                    |   '__init__': func    |
                                    | }                     |
                                     -----------------------

    -----------------               -----------------------
    | my_cat    | ───────────────→ | Instance object       |
    -----------------              | __class__ = Cat       |
                                   | __dict__ = {          |
                                   |   'name': 'Whiskers'  |
                                   | }                     |
                                    -----------------------
    ```

#### Class variable (Static) vs. Instance variable (Non-static)
- **Class variable**:
    ```
    class Dog:

        tricks = []             # mistaken use of a class variable

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks                # unexpectedly shared by all dogs
    ['roll over', 'play dead']
    ```
- **Instance Variable**
    ```
    class Dog:

        def __init__(self, name):
            self.name = name
            self.tricks = []    # creates a new empty list for each dog

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks
    ['roll over']
    >>> e.tricks
    ['play dead']
    ```

#### Method Objects
- From Python's documentation, methods work as follows. When a **non-data attribute of an instance** is *referenced*, the *instance’s class is searched*. If the name denotes a valid class attribute that is a function object, references to **both the instance object and the function object** are packed into *a method object*. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.
- Code 
    ```
    x.f()
    xf = x.f
    while True:
        print(xf()) # x.f() ~= MyClass.f(x)
    ```

#### Class method (@classmethod) and Static method (@staticmethod)
- There are differences among `foo`, `class_foo`, and `static_foo`:
    ```
    class A(object):
        def foo(self, x):
            print (f"executing foo({self}, {x})")

        @classmethod
        def class_foo(cls, x):
            print (f"executing class_foo({cls}, {x})")
        
        @staticmethod
        def static_foo(x):
            print (f"executing static_foo({x})")

    a = A()
    ```
- Group `a.foo(1)` & `a.class_foo(1)` & `A.class_foo(1)`: the class of object instance or the class itself is implicitly passed as **1st arg (`cls`) if passing class else (`self`)**.
    ```
    a.foo(1)
    a.class_foo(1)
    A.class_foo(1)
    # Output
    # executing foo(<__main__.A object at 0xb7dbef0c>, 1)
    # executing class_foo(<class '__main__.A'>, 1)
    # executing class_foo(<class '__main__.A'>, 1)
    ```

- Group `a.foo` & `a.foo(1)` (**No arg(s) passed**):
    ```
    a.foo
    a.foo(1)
    # Same output
    ```

- Group `a.class_foo` & `A.class_foo` (**No arg(s) passed**):
    ```
    a.class_foo
    A.class_foo
    # Same output: <bound method A.class_foo of <class '__main__.A'>>
    ```

- Group `a.static_foo(1)` & `A.static_foo("hi")`: neither `self` nor `cls` is implicitly passed as *1st arg*. They behave like **plain function** except that you can tell them from an instance or the class
    ```
    a.static_foo(1)
    # executing static_foo(1)

    A.static_foo('hi')
    # executing static_foo(hi)
    ```

#### Do all custom-defined classes inherit from <class 'object'> (superclass)?
    ```
    class ClassicSpam:
        pass

    class NewSpam(object):
        pass

    class Spam():
        pass

    print (ClassicSpam.__mro__)
    print (NewSpam.__mro__)
    print (Spam.__mro__)
    ```
- In all three ways to declare/define a new class (including classic style and new ones) in **Python 3+**, they all inherit from <class 'object'>.
- The answer is **Yes**.

#### Is it required to define __init__ in a Python class?
- The answer is **No**. `__init__()` is **not the constructor** in Python. It's the **initializer**.
- The real **constructor** is `__new__()`.
- Since each class inherits from <class 'object'>, even though we do not define or call, `__new__()` always allocates a blank instance on the *heap* and Python's `object.__init__()` fills by default.
- **Override** `__new__()` to create an *immutable tuple*:
    ```
    class Point2D(tuple):
        def __new__(cls, x, y):
            # Create the actual tuple data
            return super().__new__(cls, (x, y))

        def __init__(self, x, y):
            print(f"Point2D initialized with x={x}, y={y}")

        def __repr__(self):
            return f"Point2D(x={self[0]}, y={self[1]})"
    
    p = Point2D(3, 4)
    print(p)
    # Output:
    # Point2D initialized with x=3, y=4
    # Point2D(x=3, y=4)
    ```
    - If we skip *overriding* `__new__()`:
    ```
    class BadPoint(tuple):
    def __init__(self, x, y):
        self.x = x  # ERROR: tuple is immutable
    
    p = BadPoint(1, 2)  # 💥 Fails
    ```
    - In `class SubclassName(superclass)`, `Point2D` and `BadPoint` both inherit from Python's <class 'tuple'>.
- More refs: https://docs.python.org/3/reference/datamodel.html#object.__new__

#### Are Private methods truly **Private**?
- The answer is **No**, we still can access by calling `_className__nameOfPrivateMethod`
- **Safe encapsulation - mangling**: by defining `__update = update`, this makes `self.__update` become `self._Mapping__update`. Therefore, even if `update()` is overriden in a subclass, the parent class has no impact.
    ```
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update   # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)

        __update = update

    print (newMapping._Mapping__update)
    print (newMappingSubclass._Mapping__update) # Inherit Mapping.update
    print (newMappingSubclass._MappingSubclass__update)
    # Output
    # <bound method Mapping.update of <__main__.Mapping object at 0x000002D241F37350>>
    # <bound method Mapping.update of <__main__.MappingSubclass object at 0x000002D241F373D0>>

    newMapping._Mapping__update([5,6])
    newMappingSubclass.update([5],[6])

    print (newMapping.items_list)
    print (newMappingSubclass.items_list)
    # Output
    # [1, 2, 3, 4, 5, 6]
    # [(1, 2), (3, 4), (5, 6)]

    print (newMapping.update)
    print (newMappingSubclass.update)
    # Output
    # <bound method Mapping.update of <__main__.Mapping object at 0x00000226F83271D0>>
    # <bound method MappingSubclass.update of <__main__.MappingSubclass object at 0x00000226F8327250>>

    print (newMapping.__update)
    # Fail, since `__update` is defined as a private method in <class Mapping>
    ```

#### Dataclasses (@dataclass)
##### Constructor & Object Display
- Instead of using `__init__`, adding `@dataclass` can auto-fill an object with data. The following codes are equivalent
    ```
    class Person1:
        def __init__(self, name="", age=0, job=""):
            self.name = name
            self.age = age
            self.job = job

    person1 = Person1("Kai", 25, "Python Dev")

    @dataclass
    class Person2:
        name: str = ""
        age: int = 0
        job: str = ""
    person2 = Person2("Kai", 25, "Python Dev")
    # Person2(name='Kai', age=25, job='Python Dev')
    ```
- Since `@dataclass` overrides `__repr__`, it hides the **id** of an object, instead, it displays the whole object with attributes and props.

##### Object Comparing
- Resource: https://www.geeksforgeeks.org/data-classes-in-python-set-5-post-init/
- `__post_init__`: when certain attributes are dependent on the parameters passed in the `__init__()` but do not get their values directly from them. That is, they get their values after performing some operation on a subset of arguments received in the constructor.
    ```
    from dataclasses import dataclass, field 
    name = {'vibhu4agarwal': 'Vibhu Agarwal'} 

    @dataclass
    class GfgArticle: 

        title : str
        language: str
        author: str
        author_name: str = field(init = False) 
        upvotes: int = 0

        def __post_init__(self): 
            self.author_name = name[self.author] 


    dClassObj = GfgArticle("DataClass", "Python3", "vibhu4agarwal") 
    print(dClassObj) 
    # GfgArticle(title=’DataClass’, language=’Python3′, author=’vibhu4agarwal’, author_name=’Vibhu Agarwal’, upvotes=0)
    ```
    - `author_name` is dependent on profile handle which author attribute receives, so using `__post_init__()` should be used in this case.
- In this context, 
    ```
    @dataclass(order=True)
    class Person2:
        sort_index: int = field(init=False, repr=False)
        name: str = ""
        age: int = 0
        job: str = ""
        def __post_init__(self):
            self.sort_index = self.age
    person2 = Person2("Kai", 25, "Python Dev")
    person3 = Person2("Cai", 20, "Java Dev")
    print (person2 > person3)
    ```

#### Type Annotations
- Resource: https://stackoverflow.com/questions/43233535/explicitly-define-datatype-in-python-function
- One example of type annotation usage is **Fast API** framework.
- Code sample:
    ```
    def add(x: float, y: float) -> float:
        return x+y
    ```

#### Scopes
    ```
    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)

    # Output:
    # After local assignment: test spam
    # After nonlocal assignment: nonlocal spam
    # After global assignment: nonlocal spam
    # In global scope: global spam
    ```
#### Extra sources
- https://stackoverflow.com/questions/17134653/difference-between-class-and-instance-methods
- https://medium.com/@ryan_forrester_/class-methods-vs-static-methods-in-python-a-clear-guide-47fcfd385e27
