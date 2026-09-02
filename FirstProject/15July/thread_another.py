import threading
class MyThread(threading.Thread):
    def run(self):
        print("Run() method started ..")
        print("Thread Name: ", threading.current_thread().name)

thread3=MyThread()
thread3.start()
