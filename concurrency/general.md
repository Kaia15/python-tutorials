### Concurrency in Python

#### Core (Processor)
- Definition: The actual hardware unit inside a CPU that executes the instructions. There are multiple cores in modern CPUs(s).
Each core can run one thread at a time (however, with the hyper-threading technique, which makes a single core appear as two logical cores, there might be two threads running on the same core at a time).

#### Thread
- Definition: the smallest unit of execution within a process. 
- Property: 
    Multiple threads from one process share memory and resources, but they have their own instruction pointers, stacks, and registers.
    - One example of a multi-threading process: **Microsoft Word**
        - Thread 1: Format the text.
        - Thread 2: process the inputs.
        - Thread 3: control users' clicking, typing, and scrolling.
          
      ![image](https://github.com/user-attachments/assets/f49e769d-d8e6-4287-8fc1-17a44255d165)
    
    - Code: 
    ```
    import threading
    import os

    def task1():
        print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
        print("ID of process running task 1: {}".format(os.getpid()))

    def task2():
        print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
        print("ID of process running task 2: {}".format(os.getpid()))

    def main():

        print("ID of process running main program: {}".format(os.getpid()))

        print("Main thread name: {}".format(threading.current_thread().name))

        t1 = threading.Thread(target=task1, name='t1')
        t2 = threading.Thread(target=task2, name='t2')

        t1.start()
        t2.start()

        print (f"The number of alive threads is {threading.active_count()}")

        t1.join()
        t2.join()

    main()

    # Output: 
    # ID of process running main program: 10392
    # Main thread name: MainThread
    # Task 1 assigned to thread: t1
    # ID of process running task 1: 10392
    # Task 2 assigned to thread: t2
    # The number of alive threads is 3
    # ID of process running task 2: 10392

    ```

- **Daemon** Thread:
- **Same core** or **Different Cores**:
    - Code:
    ```
    ```
    - Different cores:
      


      
##### Threading Library
##### AsyncIO

#### Process
##### Visualize multi-processes
- Ref: https://medium.com/pythoneers/visualize-your-multiprocessing-calculations-in-python-with-parallelbar-5395651f35aa
- 
##### Threads vs Processes


#### GIL (Global Interpreter Lock)
##### What is GIL
##### GIL's role in blocking threads


#### Multi-threading vs Multi-processing
- Multi-processes in separate cores: 
    https://youtu.be/ljLEHY2YU1Y

    ```
    import multiprocessing
    import os
    import time
    from tqdm import tqdm
    from multiprocessing import Manager

    def worker(core_id, position):
        # Set CPU affinity (Unix only)
        try:
            os.sched_setaffinity(0, {core_id})
        except AttributeError:
            pass  # Not available on Windows

        total = 100
        with tqdm(total=total, position=position, desc=f"Core {core_id}", leave=True) as pbar:
            for _ in range(total):
                time.sleep(0.05)  # Simulate work
                pbar.update(1)

    if __name__ == '__main__':
        multiprocessing.set_start_method('fork')  # Required on macOS/Linux
        processes = []
        for i in range(4):
            p = multiprocessing.Process(target=worker, args=(i, i))
            processes.append(p)
            p.start()
    ```
- 
##### Can a thread (from process A) and whole process B run on the same core (processor)?
##### Which threads often require GIL, and which ones do not?

#### C-extension or Native C (Numpy) and Multi-threading

