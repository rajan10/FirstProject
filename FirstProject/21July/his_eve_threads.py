import threading
import time

def task_1():
    print("task-1 started")
    time.sleep(3)
    print("task-1 finished")

def task_2():
    print("task-2 started")
    time.sleep(2)
    print("task-2 finished")

threading.Thread(target=task_1).start()
threading.Thread(target=task_2).start()
help(threading.Thread)
type(threading.Thread)

