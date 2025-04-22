*Analogy*: **Numpy Array** is an *egg carton*, which holds *only eggs, same shape and size*. Since all the eggs in the same pack, we can take them order by order (by offset & size). **Python List** is a *box of mixed stuff*, which can hold anything including *an egg, a spoon, a book, a USB stick*. Each item has it *own label*, and might be *randomly* stored.

### Memory Allocation for Python List (Array)

#### Code 
```
a = [1.0, 2.0, 3.0] # a is an array defined as global variable
```

#### Diagram
  ```
  Globals:
  | a  --------------------->|------\

  Heap:

  | List object (a)                    |  <- Python list object
  | - size: 3                          |
  | - capacity: 4 or more              |
  | - pointer array (ob_item) ------->|------\
  |                                   |       \

  | ob_item[]:                  |     |        |
  |  [ptr1, ptr2, ptr3, ...]    |     |        |

      |      |      |                 |        |
      V      V      V                 |        |
    1.0    2.0    3.0  (Python float objects) <-
      |      |      |
      V      V      V
    Heap  Heap   Heap
  ```

#### Analysis
- Each element of **Python List** is a separate **Python Object** allocated in *Heap*. 
- The list stores an array of pointers to these objects, and this array is also on the *Heap*. Those Python Objects (or element in the list)' memory locations are **not neccessarily continuous**. (in the context above, the type of *PyObject* is *float*).
- This matches *Design Philosophy* in Python, which prefers *Flexibility* over *Speed*.

### Memory Allocation for Numpy Array (Python Library)

#### Code
```
import numpy as np
arr = np.array([1.0, 2.0, 3.0])
```
#### Diagram

  ```
  Globals:

  |-----------------|
  |-------arr-------|
  |-----------------|------\

                              \

  Heap:

  | NumPy array object (PyObject)  | <- metadata for `arr`
  | - shape: (3,)                  |
  | - dtype: float64              |
  | - strides, etc.               |
  | - data pointer -------------->|----\
  |                               |     |
  
  |      Raw Data Buffer        |     |
  | 1.0 | 2.0 | 3.0             |<----/
  ```

#### Analysis
- Since **Numpy** is designed to leverage *C-level* performance and follow *SIMD instruction*, its array is **raw buffer of fixed sized**. 

- To *allocate* **Numpy Array's size**, we use `np.append()` or create a new Numpy array using `np.resize()`. 
    - For `np.append()`, it is more complicated than we expect. Under the hood, it deep copies the old array/list and add more elements into a new array.

        ```
        def np_append(a, values):
            a = np.asarray(a)
            values = np.asarray(values)
            
            # Flatten if multidimensional
            a = a.ravel()
            values = values.ravel()
            
            # Allocate new memory
            new_array = np.empty(len(a) + len(values), dtype=a.dtype)
            
            # Copy data
            new_array[:len(a)] = a
            new_array[len(a):] = values
            
            return new_array

        ```

    - For `np.resize()`, the followings are conceptually steps under the hood:
        - Flatten the array if needed (under some conditions constrainted to the size of old array and the size of new array).
        - Title/Truncate the elements to fill the requested size.
        - Return a new array with desired shape.

- Because of its different way to allocate memory, the application of **Numpy Array** is *vectorization*, where we can map each element in the array buffer to apply a function *f* and return *f(x_i)* in *1-D Numpy Array* at once.
