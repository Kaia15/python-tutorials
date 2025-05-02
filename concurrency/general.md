### Concurrency in Python

#### Core (Processor)
- Definition: The actual hardware unit inside a CPU that executes the instructions. There are multiple cores in modern CPUs(s).
Each core can run one thread at a time (however, with the hyper-threading technique, which makes a single core appear as two logical cores, there might be two threads running on the same core at a time).

#### Thread
- Definition: the smallest unit of execution within a process. 
- Property: 
    Multiple threads from one process share memory and resources but have their own instruction pointers, stacks, and registers.
    - One example of a multi-threading process: **Microsoft Word**
        - Thread 1: Format the text.
        - Thread 2: process the inputs.
        - Thread 3: control users' clicking, typing, and scrolling.
          
      ![image](https://github.com/user-attachments/assets/f49e769d-d8e6-4287-8fc1-17a44255d165)
    
    - Code: Initialize **2 different threads** in the **same process (pid)**. 
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
- **Same core** or **Different Cores**?
  - We can bind a process to a CPU core, but we cannot bind a thread to a specific CPU core. Therefore, a thread is executed by which CPU core, depending on O.S scheduling. 
  - Ref: https://stackoverflow.com/questions/41401490/how-to-limit-number-of-cores-with-threading
      
##### Threading Library
##### AsyncIO

#### Process
##### Visualize multi-processes
- Ref: https://medium.com/pythoneers/visualize-your-multiprocessing-calculations-in-python-with-parallelbar-5395651f35aa
- By using `Pool`, we can *spawn* a new process created by `multiprocessing` library in Python.
  ```
    from multiprocessing import Process, Queue
    from tqdm.notebook import tqdm
    import time
    import os
    import queue
    
    NUM_WORKERS = 4
    TOTAL_STEPS_PER_WORKER = 20
    
    def worker(worker_index, progress_queue):
        pid = os.getpid()
        for _ in range(TOTAL_STEPS_PER_WORKER):
            time.sleep(0.1)  # Simulate work
            progress_queue.put((worker_index, pid, 1))
        progress_queue.put((worker_index, pid, 'done'))
    
    def display_progress(progress_queue, num_workers, total_steps):
        pbar_dict = {}
        pid_map = {}
    
        done_flags = [False] * num_workers
        while not all(done_flags):
            try:
                worker_index, pid, msg = progress_queue.get(timeout=0.5)
                if worker_index not in pbar_dict:
                    # First message from this worker — create its bar
                    pid_map[worker_index] = pid
                    pbar_dict[worker_index] = tqdm(
                        total=total_steps,
                        desc=f"Worker {worker_index} (PID {pid})",
                        position=worker_index
                    )
    
                if msg == 'done':
                    done_flags[worker_index] = True
                else:
                    pbar_dict[worker_index].update(msg)
    
            except queue.Empty:
                continue
    
    if __name__ == '__main__':
        progress_queue = Queue()
    
        # Start workers
        workers = []
        for i in range(NUM_WORKERS):
            p = Process(target=worker, args=(i, progress_queue))
            p.start()
            workers.append(p)
    
        # Main process tracks and shows progress
        display_progress(progress_queue, NUM_WORKERS, TOTAL_STEPS_PER_WORKER)
    
        for p in workers:
            p.join()

  ```
  ![progress-bar-per-process](https://github.com/user-attachments/assets/ee50305a-8924-4fac-9206-77c12d9ec58a)


##### Threads vs Processes


#### GIL (Global Interpreter Lock)
- Threads are generally 'lighter' than processes, and can be created, destroyed, and switched between faster than processes. They are normally preferred for taking advantage of multicore systems. However, multithreading with Python has a key limitation: the Global Interpreter Lock (GIL). For various reasons (a quick web search will turn up copious discussion, not to say argument, over why this exists and whether it's a good idea), **Python is implemented in such a way that only one thread can be accessing the interpreter at a time. This means only one thread can be running Python code at a time**. This almost means that you don't take any advantage of parallel processing at all. The exceptions are few but important: **while a thread is waiting for IO (for you to type something, say, or for something to come in the network), Python releases the GIL so other threads can run**.
  
##### What is GIL
- **Global Interpreter Lock** ensures that **only one thread executes Python bytecode at a time**
##### GIL's role in blocking threads
- Because of its property, we prefer to use `threading` for I/O tasks, and Python will release GIL for those tasks to implement parallelism (context switch). For CPU-bound tasks, we should not use `threading` (multithreading) due to the limitation of GIL. Instead, we will use `multiprocessing` (explained later on) to allow each process to have its own GIL and not be blocked by others.
- Multi-threads release GIL (not require execute Python bytecode - I/O task)
    ```
    import threading
    import time

    def io_bound():
        print(f"[{threading.current_thread().name}] Starting I/O task")
        time.sleep(2)
        print(f"[{threading.current_thread().name}] Done")

    start = time.time()

    threads = [threading.Thread(target=io_bound) for _ in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print("I/O-bound total time:", round(time.time() - start, 2), "seconds")
    # [Thread-1 (io_bound)] Starting I/O task
    # [Thread-2 (io_bound)] Starting I/O task
    # [Thread-1 (io_bound)] Done
    # [Thread-2 (io_bound)] Done
    # I/O-bound total time: 2.0 seconds
    ```
    - Total time is 2 seconds (GIL does not block any thread), not 4 seconds.

- Ref: https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html

#### Multi-threading vs Multi-processing
- Multi-processes in separate cores: 

  https://github.com/user-attachments/assets/63ed1f2b-1514-45b1-8e4e-49c56ff9ccbc
    
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

