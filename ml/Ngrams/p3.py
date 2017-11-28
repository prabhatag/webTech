from nltk.corpus import inaugural, stopwords
from nltk import word_tokenize

stop_words = set(stopwords.words('english'))
text = inaugural.raw("2009-Obama.txt")
wordlist  = word_tokenize(text)

wordlist = [ word for word in wordlist if word not in stop_words]
distinct_words = set(wordlist)

print("Total no. of tokens:" , len(wordlist))
print("Total no. of distinct_words:", len(distinct_words))