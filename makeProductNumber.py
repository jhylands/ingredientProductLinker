#Python file to make the numbers asociated with each word
import pickle
import re
with open('products_titles.pkl','rb') as f:
	products = pickle.load(f)
print("products length: %d"%len(products))
counter = 0
words = {}
pattern = re.compile('([^\s\w]|_)+')
strippedList = lambda x:pattern.sub('', x)
for p,q in products:
	for word in strippedList(p).split(' '): # need to check the extent to which this works
		if not word in words:
			counter+=1
			words[word] = counter

print(words.keys())
productNumbers = [[words[word] for word in strippedList(p).split(' ')] for p,q in products]
with open('productNumberLists.pkl','wb') as f:
	pickle.dump(productNumbers,f)
productNumbers.sort(key=lambda x:len(x))
with open('OrderedproductNumberLists.pkl','wb') as f:
	pickle.dump(productNumbers,f)
