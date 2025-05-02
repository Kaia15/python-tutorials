# import threading
# import time

# def io_bound():
#     print(f"[{threading.current_thread().name}] Starting I/O task")
#     time.sleep(2)
#     print(f"[{threading.current_thread().name}] Done")

# start = time.time()

# threads = [threading.Thread(target=io_bound) for _ in range(2)]
# [t.start() for t in threads]
# [t.join() for t in threads]

# print("I/O-bound total time:", round(time.time() - start, 2), "seconds")
# [Thread-1 (io_bound)] Starting I/O task
# [Thread-2 (io_bound)] Starting I/O task
# [Thread-1 (io_bound)] Done
# [Thread-2 (io_bound)] Done
# I/O-bound total time: 2.0 seconds

import threading
import time

def cpu_heavy():
    print(f"[{threading.current_thread().name}] Starting CPU task")
    count = 0
    for _ in range(50_000_000):  # Heavy CPU loop
        count += 1
    print(f"[{threading.current_thread().name}] Done")

start = time.time()

threads = [threading.Thread(target=cpu_heavy) for _ in range(1)]
[t.start() for t in threads]
[t.join() for t in threads]

print("CPU-bound total time:", round(time.time() - start, 2), "seconds")
# PS C:\Users\alice\python-tutorials\concurrency> python gil.py
# [Thread-1 (cpu_heavy)] Starting CPU task
# [Thread-2 (cpu_heavy)] Starting CPU task
# [Thread-1 (cpu_heavy)] Done
# [Thread-2 (cpu_heavy)] Done
# CPU-bound total time: 2.05 seconds
# PS C:\Users\alice\python-tutorials\concurrency> python gil.py
# [Thread-1 (cpu_heavy)] Starting CPU task (1 task)
# [Thread-1 (cpu_heavy)] Done
# CPU-bound total time: 1.0 seconds