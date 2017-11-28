from nltk.corpus import inaugural, stopwords
from nltk import word_tokenize
from string import punctuation

stop_words = set(stopwords.words('english')) | set(punctuation)
obamatext = inaugural.raw("2009-Obama.txt")
obamalist = word_tokenize(obamatext)
obamalist = [word for word in obamalist if word not in stop_words]

def getNGrams(input_list, n):
	return [' '.join(input_list[i:i+n]) for i in range(len(input_list)-(n-1))]

def getallNGram(input_list):
	allngrams = dict()
	for i in range(1,5):
		allngrams[str(i) + "_gram"] = getNGrams(input_list, i)
	return allngrams

def MostCommon(ngrams):
	for k in ngrams.keys():
		d = dict()
		for v in ngrams[k]:
			d[v] = ngrams[k].count(v)
		print(sorted(d, key = lambda x : d[x], reverse = True)[:5], '\n')

ngrams = getallNGram(obamalist)
MostCommon(ngrams)