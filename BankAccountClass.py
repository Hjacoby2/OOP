# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal #attribute, the name is balance

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount): #mutator method
        self.__balance += amount #increasing balance by amount given by user

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount): #mutator, change total amount
        if amount > self.__balance:
          print('Insufficient funds!')
        else:
          self.__balance -= abs(amount)


      # The get_balance method returns the
      # account balance.

    def get_balance(self): #accessor
        return self.__balance



    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
