from nltk import word_tokenize

f = open("input1.txt").read()
wordlist  = word_tokenize(f)

#print(wordlist)

def getNGrams(input_list, n):
	#print([' '.join(input_list[i:i+n]) for i in range(len(input_list)-(n-1))])
	return [' '.join(input_list[i:i+n]) for i in range(len(input_list)-(n-1))]

def getCount(s):
	d = dict()
	for e in s:
		c = s.count(e)
		d[e] = c
	return d

s = getNGrams(wordlist, 3)
print(s)
print()
print(getCount(s))

'''

 for i in range(len(l)-2):
...  for j in range(3):
...   print(l[i+j],sep=', ')
...  print()
... 
>>> [l[i+j] for i in range(len(l)-2) for j in range(3)]

>>> [(l[i],l[i+1]) for i in range(len(l)-1)]
[('Do', 'you'), ('you', 'like'), ('like', 'to'), ('to', 'sing'), ('sing', '?')]

'''
