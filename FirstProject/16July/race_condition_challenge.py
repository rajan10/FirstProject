import threading
import queue
from custom_exception import InvalidAmountError,BankError

class BankAccount():
    def __init__(self,name, balance):
        self.name=name
        self.balance=balance
        self.transactions=[]
        # Thread synchronization
        self.lock=threading.Lock()
        self.results=queue.Queue()

    def deposit(self, amount):
        thread_name=threading.current_thread().name
        print(f"{thread_name} : Depositing : {amount}")
        try:
            with self.lock:
                if amount<0:
                    raise InvalidAmountError("Deposit must be greater than zero!")
                self.balance=self.balance+amount
                transaction={"thread":thread_name,
                                "operation":"Deposit",
                                "amount":amount,
                                "balance":self.balance,
                                "status":"Success"}
                result=(thread_name, True, f"deposit {amount} successful!")
             
                transaction={"thread":thread_name,
                                "operation":"Deposit",
                                "amount":amount,
                                "balance":self.balance,
                                "status":"Failure"}
                self.transactions.append(transaction)
                result=(thread_name, True, f"deposit {amount} successful!")  
                self.results.put(result) 
        except BankError as e:
                print(f"{e.message}:{e.code}")
                transaction={"thread":thread_name,
                                "operation":"Deposit",
                                "amount":amount,
                                "balance":self.balance,
                                "status":"Failed",
                                "reason":str(e)}
                result=(thread_name, False, str(e))
                self.results.put(result)
                self.transactions.append(transaction)
    def withdraw(self, amount):
        thread_name=threading.current_thread().name
        print(f"{thread_name} : Withdrawing : {amount}")
        try:
            with self.lock:
                if amount <= self.balance and amount > 0:
                    self.balance=self.balance-amount
                    transaction={"thread":thread_name,
                                 "operation":"withdraw",
                                 "amount":amount,
                                 "balance":self.balance,
                                 "status":"Success"}
                    result=(thread_name, True, f"Withdraw {amount} successful!")
                else: 
                    transaction={"thread":thread_name,
                                 "operation":"withdraw",
                                 "amount":amount,
                                 "balance":self.balance,
                                 "status":"Success"}
                    result=(thread_name, True, f"Withdraw {amount} successful!")
                self.results.put(result)
        except Exception as e:
            
            result=(thread_name, False, f"Exception raised")
        self.transactions.append(transaction)
    def display(self):
        print("Transactions displayed")
        print("\n ======================Final Report =====================" )
        print("Account holder Name:",self.name)
        print("Balance:", self.balance)
        print("\n Thread results \n")
        for transaction in self.transactions:
            print(transaction)
        while not self.results.empty():
            print(self.results.get())
        
    
            
ram_bank_account=BankAccount("Ram",1000)  
t1=threading.Thread(target=ram_bank_account.deposit, args=(-100,),name="thread-1")
t2=threading.Thread(target=ram_bank_account.withdraw, args=(100,),name="Thread-2")
t3=threading.Thread(target=ram_bank_account.withdraw, args=(100,),name="Thread-3")

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
ram_bank_account.display()