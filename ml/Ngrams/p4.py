from nltk.corpus import inaugural, stopwords
from nltk import word_tokenize
from string import punctuation

stop_words = set(stopwords.words('english')) | set(punctuation)
obamatext = inaugural.raw("2009-Obama.txt")
georgetext = inaugural.raw("1789-Washington.txt")
obamalist = word_tokenize(obamatext)
georgelist = word_tokenize(georgetext)
obamalist = [word for word in obamalist if word not in stop_words]
georgelist = [word for word in georgelist if word not in stop_words]

obamalistTop50 = sorted(set(obamalist), key = lambda x : obamalist.count(x), reverse = True)[:50]
georgelistTop50 = sorted(set(georgelist), key = lambda x : georgelist.count(x), reverse = True)[:50]

#print(obamalistTop50, '\n')
#print(georgelistTop50)


print("Obama Top 50")
for e in obamalistTop50:
	print(e, obamalist.count(e))
print("\nGeorge Top 50")
for e in georgelistTop50:
	print(e, georgelist.count(e))