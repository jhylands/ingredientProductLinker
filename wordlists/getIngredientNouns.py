
from ingToPro import getStructure
import pickle
from wordType import wordType as wt

#functions 
def tryWord(word,wordType):
	try:
		return wordType(word)
	except:
		return 'u.'
def tryStructure(text):
	try:
		return getStructure(text)
	except:
		return {'name':''}

#gathering data
def main():
    with open('products.pkl','rb') as f:
        products = pickle.load(f)
    with open('ingredients.txt','r') as f:
        ingredients = f.read().split('\n')
    #main
    wordType = wt()
    structured_ingreients = [tryStructure(ingredient) for ingredient in ingredients]
    w = [' '.join([tryWord(word,wordType) for word in i['name'].split(' ')]) for i in structured_ingreients]
    return w, structured_ingreients
