#### Iterable
- An object capable of returning its members one at a time. 
- Examples of **iterables** include **sequence** types: `list`, `str`, `tuple`
#### Diagram
```
[ An Iterable ]
   |
   |-- must have --> __iter__() --> [ Returns an Iterator ]
                                           |
                                           |-- must have --> __next__() 
```
#### Iterable Protocol
- Definition: A simple set of rules (*methods*) that an object must follow if you want it to be *looped over* (used in `for` loops, `list(), sum()`, etc.).
- **List**: Since the *Iterable Protocol* is hidden-ish, and does not inherit from **Iterable class**, `__iter__()` does not display in `list.__mro__`, but `hasattr(list_instance, '__iter__')` is correct (just `__iter__` is not called).

#### It seems to be contradict?
- **Contradict**: `__iter__()` is explicitly triggered when Python calls `iter()` to get an iterator object & delay the computation until `__next__()` is called. Meanwhile, `for` loop is applied in a **iterable** list, it produces the element immediately.
- **Explanation**: Iterables can be used in a `for` loop and in many other places where a sequence is needed (`zip(), map()`, …). When an iterable object is passed as an argument to the built-in function `iter()`, it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call `iter()` or deal with iterator objects yourself. The `for` statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. **Summarize mechanism**:
    - `iter(lst)`: Creates an iterator from the list, but does not start iteration.
    - `next(iterator)`: Asks for the next item from the iterator.
    - `for item in lst`: Internally does: `it = iter(lst) then while True: next(it)` for each item **automatically**.

### Iterator
    ```
    s = 'abc'
    itr = iter(s)
    next(itr)
    # 'a'
    next(itr)
    # 'b'
    next(itr)
    # c
    next(itr)
    # StopIteration 
    ```
- We can also add iterator behavior to our classes:
    ```
    class Reverse:
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]
    ```
### Generator
- `yield`: Create an Iterator object to delay the computation (apply laziness) until called.
    ```
    def basic_gen(): 
        yield 1
        yield 2

    print(basic_gen())
    # <generator object basic_gen at 0x000002680F04A810>

    for i in basic_gen():
        print(i)
    # 1
    # 2

    # we can also use next() with generator objects
    basic_gen = basic_gen()
    print(next(basic_gen))
    # 1
    ```

    ```
    class NumberFromSequence:
        # we get numbers daily in a string
        def __init__(self, daily_results: str) -> None:
            self.daily_results = daily_results
            
        def __iter__(self):
            # make it more lazy - not storing list of numbers to attribute
            for number in self.daily_results.split(' '):
                yield number # no need to explicit return
                
    nums = NumberFromSequence('20 31 21 54 90')
    for i in nums:
        print(i)
    ```
- Example (Memory Saved): `yield` is best used when you have a function that returns a sequence and you want to iterate over that sequence, but you do not need to have every value in memory at once.
    - For example, I have a python script that parses a large list of CSV files, and I want to return each line to be processed in another function. I don't want to store the megabytes of data in memory all at once, so I `yield` each line in a python data structure. So the function to get lines from the file might look something like:
    ```
    def get_lines(files):
        for f in files:
            for line in f:
                #preprocess line
                yield line
    ```

### `itertools`
