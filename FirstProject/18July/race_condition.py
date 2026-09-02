import threading

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.lock=threading.Lock()
        self.results=[]

    
    def withdraw(self, amount):
        print(f"Trying to withdraw {amount}")
        thread_name = threading.current_thread().name

        print(f"{thread_name}: Trying to withdraw {amount}")
        # self.lock.acquire()
        #  -------------- Critical Section Starts ---------------------- #
        with self.lock:
            try:
                if amount > self.balance:
                    result = (thread_name, False, "As amount is greater than balance, no sufficient fund available!")
                else:
                    self.balance -= amount
                    result = (thread_name, True, f"{amount} is withdrawn. Net balance after withdraw is : {self.balance}")
                self.results.append(result)

            except Exception as e:
                result = (thread_name, False, f"unexpected Error:{e}")
                self.results.append(result)
            # self.lock.release()
    def create_thread(self):
        self.thread1 = threading.Thread(target=self.withdraw, args=(800,),name="Thread-1")
       
        self.thread2 = threading.Thread(target=self.withdraw, args=(800,),name="Thread-2")
      
        print("threads created only- Not started ")

    def run(self):
       
        print("Thread 1 starting now ")
        self.thread1.start()
    
        print("Thread 2 starting now ")
        self.thread2.start()

        self.thread1.join()
        self.thread2.join()
         
    def display(self):
        print("The final balance is: ", self.balance)
        for result in self.results:
            print(result)
          
ram_bank_account= BankAccount("Ram",1500)
ram_bank_account.create_thread()
ram_bank_account.run()

ram_bank_account.display()
# ram_bank_account.start()
# ram_bank_account.start()
# thread1= t1.withdraw(100)
# thread2=t2.withdraw(200)