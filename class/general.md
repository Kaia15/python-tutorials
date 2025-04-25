
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

#### Class variable (Non-static) vs. Instance variable (Static)

#### Class method vs. Instance method

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
- The answer is **No**, we still can access by calling `_className__nameOfPrivateMethod`
- **Safe encapsulation - mangling**: by defining `__update = update`, this makes `self.__update` become `self._Mapping__update`. Therefore, even if `update()` is overriden in a subclass, the parent class has no impact.

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
    ```
