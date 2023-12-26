from bank_accounts_25 import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(100)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)
