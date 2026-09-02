import threading
import time

def task1():
    print("Downloading")
    # time.sleep(3)
    print("Task-1 completed")

def task2():
    print("Playing Music")
    # time.sleep(2)
    print("Task-2 completed")

thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)
# task1()
# task2()
thread1.start()
thread2.start()

print("All tasks completed")

