### Primitive Types as Object

- Unlike other languages like **Java,C**, Python treats all types, including *primitive types* as *PyObject*.
- This is why each time we print out the type of a variable, the output is *class <class_name>*:
```
x = 5
print (type(x)) # Output: <class 'int'>
```

#### Specific Example: int (Python), int (Java), and Integer (Java)
- **int (Python)** is an object, and **immutable**:
    ```
    a = 8
    a = 100 # points to a different object int(100)
    ```
    - `a` first points to an `int` object with value `8`
    - Then `a` is rebound to a new `int` object with value `100`
    - The original `int(8)` isn't changed, and *cannot be changed*

- **int (Java)** is a simple, raw memory block 
    ```
    int a = 8;
    a = 100;
    ```
    - Initially, `a` is stored in 4 bytes `00000000 00000000 00000000 00001000`
    - Then, we re-assign `a = 100`, its stored bits will be changed as `00000000 00000000 00000000 01100100`

- **Integer (Java)** is a reference address pointing an object allocated in *Heap*
    ```
    Stack:
    +-----------+
    | ref to obj| ──────────────┐
    +-----------+               ↓
                            Heap:
                            +--------------+
                            | Class: Integer |
                            | value: 8       |
                            +--------------+
    ```

#### (Optional) How Python avoids to creating wasted objects?



