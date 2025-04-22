### Tupple Props:
- An *immutable, fixed-size array of pointers* to *Python objects*.
- Allocated in *one block of memory* on the heap.
- Efficient in access, but not compact like a NumPy array.

### Diagram

#### Code
```
t = (10, 20, 30)
```

```
========== STACK ==========
t  ------------------------> pointer to tuple object

========== HEAP ==========
Tuple object:
- size = 3
- ob_item = [ptr1, ptr2, ptr3]
                   |     |     |
                   V     V     V
             int(10)  int(20)  int(30)
            (heap)   (heap)   (heap)

```

### Difference between Tuple and List in Python
- Since Python is executed by *CPython*, the followings are *struct* of **Tuple** & **List**:
    - **Tuple**:
        ```
        typedef struct {
            PyObject_VAR_HEAD
            PyObject *ob_item[1]; /* actual size is dynamically allocated */
        } PyTupleObject;
        ```
        - `*ob_item` seems to be an array of size 1, but there exists **C trick** ~ **flexible array member**.
        - Python allocates **exactly enough memory** to hold the number of items in the tuple:
        ```
        /* A fixed-size array of pointers of size n */
        malloc(sizeof(PyTupleObject) + (n - 1) * sizeof(PyObject *)) 
        ```
        - **Tuple** is *immutable*.
        ```
        t = (1, 2, 3)
        t[0] = 9   # ❌ Error: 'tuple' object does not support item assignment
        ```

    - **List**
        ```
        typedef struct {
            PyObject VAR_HEAD
            PyObject **ob_item; /* pointer to dynamic array of PyObject pointers */
            Py_ssize_t allocated;
        } PyListObject;
        ```
        - `**ob_item` is a pointer to a pointer array, not an **embedded** array like tuple.
        - **List** is *mutable*.