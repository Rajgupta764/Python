class account:
    def __init__(self,balance,account_No):
        self.balance=balance
        self.account_No=account_No
    
    def credit(self):
        amout=float(input("Enter the amount:"))
        self.balance=self.balance+amout
    
    def debit(self):
        damout=float(input("Enter the amout:"))
        if(self.balance==0 | self.balance<damout):
            print("Insufficient balance you can not withdraw money")
        else:
            self.balance=self.balance-damout
    def printamount(self):
        print("The total amount is: ",self.balance)

a=account(0,76458)
a.credit()
a.printamount()
a.debit()
a.printamount()
