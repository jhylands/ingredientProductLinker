#python program to convert ingredients to products
import re as reg


def match(ingreditn):
    unit = r'(g|grams|tsp|tbsp|liters)' #match units
    ingredient_re = reg.compile(r'''
^\d+ #start with a digit
{unit}
    '''

ingridents_re = reg.compile('^(?:(\d+)\s?((?:(?:g|ml|l|kg|gram|kilogram|tsp|teaspoon|tbsp|tablespoon|liter|cup)s?))?\s)?((?:[a-z]+\s?)+)')
ingredients_re = reg.compile('^(?:((?:\d|[\u00BC-\u00BE]|[\u2150-\u215E])+)\s?((?:(?:g|ml|l|kg|gram|kilogram|tsp|teaspoon|tbsp|tablespoon|liter|cup|pint)s?))?\s)?((?:[a-z]+\s?)+)')

number_re = '(?:(?:\d|[\u00BC-\u00BE]|[\u2150-\u215E]|\.|-)+)'
unit_re = '((?:(?:cm|g|oz|ml|l|kg|gram|kilogram|tsp|teaspoon|tbspn|tbsp|tablespoon|liter|cup|pint|fl oz)s?))?'
words_re = '((?:[a-z]+\s?)+)'
ingredients_re = reg.compile('''
    ^ #start of string
    ({num}) #capture the ammount
    \s? #there may be a space between the ammount and the unit
    ({unit})? #there may be a unit

    (\s?\/\s? the ammount might be represented in two units
        ({num})
        \s?
        ({unit}?)
    )?
    \s #there is then a space
    ({words}) #one or more words describing the item


'''.format(num=number_re,unit=unit_re,words=words_re),reg.VERBOSE)

frac_re = "(?:[\u00BC-\u00BE]|[\u2150-\u215E])"
number_re = "(?P<number>\d+\.\d+|\d\s?{frac})".format(frac = frac_re)
unit_re = '''
        (?:
            (?:cm|g|oz|ml|l|kg|gram|kilogram|tsp|teaspoon|tbspn|tbsp|tablespoon|liter|cup|pint|fl oz)s?
        )
'''
ammount_re = "(?:{num}\s?{unit}|{num}\s?{unit}?-{num}\s?{unit})".format(num = number_re,unit = unit_re)

ammount_helpful_re = "{ammount}(?:\s?\/\s?{ammount})?".format(ammount = ammount_re)

word_re = "((?:[a-z]+\s?)+)"

ingredient_re = "{help_ammount}\s{words}"
