import string
def ispanagram(str,alphabet=string.ascii_lowercase):
	alphaset=set(alphabet)
	return alphaset<=set(str.lower())

ans=ispanagram('the quick brown fox jumps over the lazy dog')	
print(ans)

                         #ANOTHER METHOD


def panagram(str):
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for x in str:
		if x.lower() in alphabet:
			y=alphabet.index(x)
			alphabet.pop(y)
		if 	alphabet==[]:
			return True

ans=panagram('the quick brown fox jumps over the lazy dog')		
print(ans)