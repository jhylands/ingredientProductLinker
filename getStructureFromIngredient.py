#python program to convert ingredients to products
import re 


class NotIngredient(Exception):
    def __init__(self,text):
        print(text)

def getStructure(ingredientText,getRegex=False):
    #define fractional numbers
    frac_re = "(?:[\u00BC-\u00BE]|[\u2150-\u215E])"

    #define a number as 
        #digits dot(maybe) digits(zero or more)
        #12.5
    #or
        #digits fraction 
        #1 ½
    number_re = "(\d\s?{frac}|\d+(?:\.\d+)?)".format(frac = frac_re)
    
    #define what text might be considered a unit
    unit_re = '''
            (
                (?:cm|g|oz|ml|l|kg|gram|kilogram|tsp|teaspoon|tbspn|tbsp|tablespoon|liter|cup|pint|fl\soz)s?
            )
    '''
    
    ammount_re = "(?:{num}\s?{unit}?\s?-\s?{num}\s?{unit}?|{num}\s?{unit}?)".format(num = number_re,unit = unit_re)

    ammount_helpful_re = "{ammount}(?:\s?\/\s?{ammount})?".format(ammount = ammount_re)
    #allowing for Crème fraîche https://stackoverflow.com/questions/1922097/regular-expression-for-french-characters
    word_re = "((?:[a-zA-ZÀ-ÿ]+\s?\'?\-?)+)"

    ingredient_re = "(?:{help_ammount}\s)?{words}".format(help_ammount = ammount_helpful_re, words = word_re)
    struc = re.compile(ingredient_re,re.VERBOSE)
    


    g = struc.search(ingredientText)
    if g is None:
        raise NotIngredient(ingredientText)
    if getRegex:
        return ingredient_re
    
    alternatives = {'amountLower':g.group(1) or g.group(5),
     'unitLower':g.group(2) or g.group(6),
     'amountHigher':g.group(3),
     'unitHigher':g.group(4),
     'alternativeAmountLower':g.group(7),
     'alternativeUnitLower':g.group(8),
     'alternativeAmountHigher':g.group(9) or g.group(11),
     'alternativeUnitHigher':g.group(10) or g.group(12)}

    

    dic  = {'name':g.group(13),
            'amount':g.group(1) or g.group(5),
            'unit':g.group(2) or g.group(6)
            }
    dic.update(alternatives)
    return dic
