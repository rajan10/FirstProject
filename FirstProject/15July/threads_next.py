import time
import threading

def download_file():
    print("Download file started ...")
    time.sleep(3)
    print("Download completed!")

t5=threading.Thread(target=download_file)
t5.start()
t5.join()

print("Read data....")