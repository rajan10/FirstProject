import threading
import time
def process_data():
    time.sleep(3)

# worker thread
thread=threading.Thread(target=process_data)

thread.start()
print(thread.is_alive())

thread.join()
print(thread.is_alive())

print(threading.current_thread().name)