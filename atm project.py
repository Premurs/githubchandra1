class ATM:
    def__init__(self,balance=1000):
        self.balance=balance



     def check_balance(self):
         return f'your account balance is ${self.balance}'



     def deposit(self,amount):
         self.balance +=amount
         return f'deposited ${amount}. your new balance is ${self.balance}'



     def withdraw(self,amount):
         if self.balance >=amount:
             self.balance -=amount
             return f'withdraaw ${amount}. your new balance is ${self.balance}'
         else:
             return 'insufficient fund.withdrawal failed.'
# create an instance of the atm
atm=ATM()
while True:
    print('1, check_balance')
    print('2, deposit')
    print('3, withdwaw')
    print('4, exit')



    choice = input('enter your choice:')


    if choice =='1':
        print(atm.check_balance())
    elif choice =='2':
        amount = float(input('enter the deposit amount:'))
        print(atm.deposit(amount))
    elif choice =='3':
        amount = float(input('enter the withdrawal amount:'))
        print(atm.withdraw(amount))
    elif choice =='4':
        print('Thank you for using the atm. Goodbye!')
        break
    else:
        print('invalid choice. please select a valid option.')
