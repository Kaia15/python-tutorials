### Memory Allocation for Python Set
- Unlike `list`, `set` in Python works as a `dict` under the hood. 

#### Code
```
s = {0, 1, 2, 3, 4, 5, 6, 7}
s.add(8)
```

#### Diagram
- Before adding `8` to `s`:
    ```
    Set Object:
    +---------------------------+
    | size: 8                   |
    | capacity: 8               |
    | table pointer ----------> |------------------\
    +---------------------------+                   |
                                                    V
                                    Hash Table (size 8 slots):
                                    +-------+--------------------------+
                                    | Index | Slot Content             |
                                    +-------+--------------------------+
                                    |   0   | EMPTY / other             |
                                    |   1   | pointer → int(3)          |
                                    |   2   | pointer → int(0)          |
                                    |   3   | pointer → int(6)          |
                                    |   4   | pointer → int(1)          |
                                    |   5   | pointer → int(7)          |
                                    |   6   | pointer → int(5)          |
                                    |   7   | pointer → int(2)          |
                                    +-------+--------------------------+

    (Load factor = 8/8 = 100% → triggers resizing)
    ```

- After adding `8`:
    ```
    Set Object:
    +---------------------------+
    | size: 9                   |
    | capacity: 16              |
    | table pointer ----------> |------------------\
    +---------------------------+                   |
                                                    V
                                    Hash Table (size 16 slots):
                                    +--------+--------------------------+
                                    | Index  | Slot Content             |
                                    +--------+--------------------------+
                                    |   0    | EMPTY                    |
                                    |   1    | pointer → int(4)         |
                                    |   2    | pointer → int(2)         |
                                    |   3    | pointer → int(5)         |
                                    |   4    | pointer → int(8)         |
                                    |   5    | EMPTY                    |
                                    |   6    | pointer → int(3)         |
                                    |   7    | pointer → int(6)         |
                                    |   8    | EMPTY                    |
                                    |   9    | pointer → int(0)         |
                                    |  10    | pointer → int(1)         |
                                    |  11    | pointer → int(7)         |
                                    |  12–15 | EMPTY                    |
                                    +--------+--------------------------+

    (Load factor = 9/16 = ~56% → good, no further resizing)
    ```

#### Does `index()` function exist in Python Set?
- The answer is **No**. Because of its special property that `set` works as a hash table, it is **unordered collection** of elements, and there is **no way for duplicates**.
- Code 
    ```
    6 in s # True, O(1) average b.c look up in hash table
    ```

#### `sorted(set(["apple", "orange", "apple", "banana"]))` means we can Sort a Set?
- The answer is **No**, `sorted()` and `.sort()` are totally different:
    - `.sort()` seems to be a private method in class *List*.
    - `sorted()` looks like **global (built-in) function**, very much like a `static` void in Java.
