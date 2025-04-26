from dataclasses import dataclass, field

class Cat:
    species = "Feline"
    def meow(self):
        print ("meow!")

my_cat = Cat()
my_cat.name = "Whiskers"

print("Class object id (Cat):", id(Cat))
print("Class __dict__ id:", id(Cat.__dict__))
print("Class attribute 'species' id:", id(Cat.species))
print("Class method 'meow' id:", id(Cat.meow))

print("Instance object id (my_cat):", id(my_cat))
print("Instance __dict__ id:", id(my_cat.__dict__))
print("Instance attribute 'name' id:", id(my_cat.name))

print (hasattr(my_cat, "species"), my_cat.__dict__)
print (my_cat.species)
print (Cat.__init__)
print (my_cat.__init__)

print(Cat.__dict__['species'] is Cat.species)  # True
print(Cat.__dict__['meow'] is Cat.meow) # True
print(Cat.__dict__['meow'] is Cat().meow) # False, since Cat() is an instance of class Cat => creates a bound method object
print(Cat.__dict__['meow'] is Cat().meow.__func__)

print (Cat.__mro__) # (<class '__main__.Cat'>, <class 'object'>)

# Output:
# Class object id (Cat): 2677133914976
# Class __dict__ id: 2677129658320
# Class attribute 'species' id: 2677129707696
# Class method 'meow' id: 2677131808256
# Instance object id (my_cat): 2677131858768
# Instance __dict__ id: 2677129707584
# Instance attribute 'name' id: 2677131767984
# True {'name': 'Whiskers'}
# Feline
# <slot wrapper '__init__' of 'object' objects>
# <method-wrapper '__init__' of Cat object at 0x0000026F517E5350>


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

newMapping = Mapping([1,2,3])

newMappingSubclass = MappingSubclass([(1, 2), (3, 4)])


print (newMapping._Mapping__update)
print (newMappingSubclass._Mapping__update)

newMapping._Mapping__update([5,6])
newMappingSubclass.update([5],[6])

print (newMapping.items_list)
print (newMappingSubclass.items_list)

print (newMapping.update)
print (newMappingSubclass.update)

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
print (a.class_foo)
print (A.class_foo)

class Person1:
    def __init__(self, name="", age=0, job=""):
        self.name = name
        self.age = age
        self.job = job

person1 = Person1("Kai", 25, "Python Dev")

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

