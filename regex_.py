# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(?:((?:\d|[\u00BC-\u00BE]|[\u2150-\u215E]|\.|-)+)\s?((?:(?:cm|g|oz|ml|l|kg|gram|kilogram|tsp|teaspoon|tbspn|tbsp|tablespoon|liter|cup|pint|fl oz)s?))?(?:\s?\/\s?((?:\d|[\u00BC-\u00BE]|[\u2150-\u215E]|\.|-)+)\s?((?:(?:cm|g|oz|ml|l|kg|gram|kilogram|tsp|teaspoon|tbspn|tbsp|tablespoon|liter|cup|pint|fl oz)s?))?)?)?\s((?:[a-z]+\s?)+)"

with open('ingredients.txt','r') as f:
    test_str = f.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
