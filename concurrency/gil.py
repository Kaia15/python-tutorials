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