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

# ID of process running main program: 10392
# Main thread name: MainThread
# Task 1 assigned to thread: t1
# ID of process running task 1: 10392
# Task 2 assigned to thread: t2
# The number of alive threads is 3
# ID of process running task 2: 10392