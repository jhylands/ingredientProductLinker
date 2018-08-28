import pickle
import re
with open('products_titles.pkl','rb') as f:
	products = pickle.load(f)


pattern = re.compile('([^\s\w]|_)+')
strippedList = lambda x:pattern.sub('', x)

words={}
counter=0
for p,q in products:
	for word in strippedList(p).split(' '):
		if not word in words:
			counter+=1
			words[word] = counter
unwords = {}
for key in words.keys():
    unwords[words[key]] = key

