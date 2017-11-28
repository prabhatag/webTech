from nltk import word_tokenize

f = open("input1.txt").read()
wordlist  = word_tokenize(f)


def getNGrams(input_list, n):
	return [' '.join(input_list[i:i+n]) for i in range(len(input_list)-(n-1))]

def getallNGram(input_list):
	allngrams = dict()
	for i in range(1,5):
		allngrams[str(i) + "_gram"] = getNGrams(input_list, i)
	return allngrams

def getProb(ngrams):
	for k in ngrams.keys():
		for e in ngrams[k]:
			print(e , ":", ngrams[k].count(e) / len(ngrams[k]))

ngrams = getallNGram(wordlist)
print(getProb(ngrams))
