def up_low(str):
	d={"upper":0, "lower":0}
	for c in s:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else: pass
	print ("original string:",s)
	print ("no. of upper case letters:",d["upper"])	
	print ("no. of lower case letters:",d["lower"])	

s="Hello tHis Is A good Day"
up_low(s)

                  #ANOTHER METHOD

def up_low(s="this is Working"):
	clow=0 
	cup=0
	for x in s:
		if x>='A' and x<='Z':
			cup +=1
		elif x>='a' and x<='z':
		    clow +=1
		
	print("lower case letters are:")
	print(clow)
	print("upper case letters are:")
	print(cup)	

up_low()                  
