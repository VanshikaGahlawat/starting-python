def unique_list(g_list):
	new=[]
	for x in g_list:
		if x not in new:
			new.append(x)
		
	print(new)

unique_list([1,1,1,1,1,2,2,2,2,3,3,3,4,5])	

			