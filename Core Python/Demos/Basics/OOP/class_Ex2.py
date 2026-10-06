class Bank_Account:
    def __init__(self,acc_num, acc_holder, balance):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.__balance = balance

    def get_Acc_num(self):
        return self.acc_num
    def set_Acc_num(self, newAccNum):
        self.acc_num = newAccNum

    def get_Acc_holder(self):
        return self.acc_holder
    def set_Acc_holder(self, newAccHolder):
        self.acc_holder = newAccHolder

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        if amount <= 0:
            print('Deposite amount must be greater than 0')
        else:
            self.__balance += amount
            print(f'Deposited : {amount}. New Balance : {self.__balance}')

    def withdraw(self,amount):
        if amount <= 0:
            print('Withdraw amount must be grater than 0')
        elif amount > self.__balance:
            print('Insufficient balance')
        else:
            self.__balance -= amount
            print(f'Withdraw : {amount}. New Balance : {self.__balance}')

    def __str__(self):
        return f'Acc No: {self.acc_num} Holder: {self.acc_holder} Balance: {self.__balance}'

acc = Bank_Account(101, 'shyam', 5000)
print(acc)    
acc.withdraw(2000)
acc.withdraw(1000)
acc.deposite(1000)
acc.withdraw(10000)
print(acc)