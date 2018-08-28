from ingToPro import getStructure
import json
import pickle
def tryGetStructure(ingredient):
    try:
        return getStructure(ingredient)
    except:
        return ingredient


def ingPro():
    with open('ingredients.txt','r') as f:
        ingredients = f.read().split('\n')
    with open('output.james','r') as f:
        products = json.loads(f.read())
    with open('recipe.pkl','rb') as f:
        recipes = pickle.load(f)
    
    ingredients_names = [tryGetStructure(p) for p in ingredients]
    return ingredients,products,recipes,ingredients_names
