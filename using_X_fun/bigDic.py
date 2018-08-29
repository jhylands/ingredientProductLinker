
#[(),()] -> ''
def convertTuplets(tupple_list):
    return' '.join([t[0] for t in tupple_list])

list_matches = []

import pickle
from getWordsDic import unwords
from functools import reduce
bigDic ={}
def getBigDic():
    return bigDic

def doStuff(row):
    #get live rows
    row = [cell for cell in row if cell!=[] and cell!=0]
    #matches_ofa_row = [matches for matches, a, b in row]
    for cell in row:
        doCellStuff(cell)


def doCellStuff(cell):
    #order strings smallest to largest
    cell.sort(key=lambda x:len(x[0]),reverse=True)
    add = lambda a,b : a+b
    elm = reduce(add,[ [ ' '.join([unwords[num] for num in seq]) for seq in block] for block in cell])
    
    #put them in the hash
    if cell==[]:
        return 1
    main_match = elm[-1]
    if main_match in bigDic.keys():
        bigDic[main_match][0] += 1
        bigDic[main_match][1] += 1
    else:
        bigDic[main_match] = [1,1]
    for match in elm[:-1]:
        if match in bigDic.keys():
            bigDic[match][0] += 1
        else:
            bigDic[match] = [1,0]

for i in range(1,42084):
    print("Opening: %d"%i)
    with open('data/%d.pkl'%i,'rb') as f:#'learning_vertulisation/searchProducts/data/%d.pkl'%i,'rb') as f:
        doStuff(pickle.load(f))
