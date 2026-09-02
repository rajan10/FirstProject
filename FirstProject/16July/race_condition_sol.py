import threading
import time
balance=1000
lock=threading.Lock()
def withdraw(amount):
    global balance
    # lock.acquire()
    with lock:
        if balance>= amount:
            print(threading.current_thread().name,"is processing withdraw")
            current_balance=balance
            time.sleep(1)
            balance=current_balance-amount
            print("Remaining balance", balance)
        else:
            print("insufficient balance")
    
        # lock.release()
t1=threading.Thread(target=withdraw, args=(700,), name="Customer-1")
t2=threading.Thread(target=withdraw, args=(700,), name="Customer-2")
t1.start()
t2.start()
t1.join()
t2.join()
print("Final blance:",balance)