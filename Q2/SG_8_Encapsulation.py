class BannAccount:
  def __init__(self, account_number: int, balance: float): #this initalizes private variables to store sensitive data
    self. __account_number = account_number
    self. __balance = 0
    self. set_account_number(account_number)
    self. set_balance(balance)

def set_account_number(self, account_number: int):
  self. __account_number = account_number

def set_balance(self, balance: float):
  if balance < 0:
    print("The balamce must not be a negative number")
  else: self. __balance = balance
