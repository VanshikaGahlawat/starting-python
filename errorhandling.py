#example 1

try:
	for i in ['a','b','c']:
		print(i**2)

except: print('There is a TypeError')

#example 2

x=5
y=0
try: z=x/y
except: print('invalid operation')
finally: print("All Done")		


#example 3
def ask():

	while True:
		
		try:
			x=int(input("enter the no. to be squared:"))
		except: 
			print("An error occurred! Please try again.")
			continue
		else: 
			break

	print("The squared no is: ",x**2)		


		  				 	