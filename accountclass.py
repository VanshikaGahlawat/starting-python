class Account:
	def __init__(self,owner,balance):
		self.owner=owner
		self.balance=balance

	def deposit(self,amount):
		self.balance+=amount
		print(f'Rs.{amount} is deposited to your account')
		print(f"new balance= Rs.{self.balance}")

	def withdraw(self,wamt):
		if(self.balance>=wamt):
			self.balance-=wamt
			print('Amount withdrawn')
			print(f'Aval bal= Rs.{self.balance}')
		else: print("Not enough amount in account")	
	def __str__(self):
		return f"account owner:{self.owner}\naccount balance:{self.balance}"


acc1=Account('Vanshika',99832.0)
print(acc1)
acc1.deposit(2000)
acc1.withdraw(10000000)					