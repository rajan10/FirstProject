import threading
import queue

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.results = queue.Queue()
        self.lock = threading.Lock()

    def withdraw(self, amount):
        thread_name= threading.current_thread().name
        print(f"{thread_name} is trying to withdraw ${amount}")
        try:
            
            with self.lock:
                            if amount > self.balance:
                                result=(thread_name, False, "Withdraw amount is greater than balance")
                               
                            else:
                                self.balance=self.balance-amount
                                result=(thread_name,True, f"{amount} withdrawn, & the net balance is: {self.balance - amount}")
                            self.results.put(result)
        except Exception as e:
            self.results.put(False, f"Error occurred, {str(e)}")
    def deposit(self, amount):
          thread_name=threading.current_thread().name
          print(f"{thread_name}is trying to deposit ${amount}")
          try:
                with self.lock:
                      self.balance=self.balance+amount
                      result=(thread_name, True, f"{amount} deposited, & the net balance is: {self.balance+amount}")
                      self.results.put(result)
          except Exception as e:
                self.results.put(False, "Exception occured", str(e))
    def display(self):
          print("\n ======================Final Report =====================" )
          print("Account holder Name:",self.name)
          print("Balance:", self.balance)
          print("\n Thread results \n")
          while not self.results.empty():
                print(self.results.get())

account =BankAccount("Ram",1000)
t1=threading.Thread(target=account.deposit, args=(500,),name="Thread-1")
t2=threading.Thread(target=account.withdraw, args=(600,),name="Thread-2")
t1.start()
t2.start()

t1.join()
t2.join()
account.display()
        







