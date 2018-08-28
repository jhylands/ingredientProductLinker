
#[(),()] -> ''
def convertTuplets(tupple_list):
    return' '.join([t[0] for t in tupple_list])

list_matches = []

import pickle


for i in range(len(products)):
    print("Opening: %d"%i)
    with open('learning_vertulisation/searchProducts/data/%d.pkl'%i,'rb') as f:
        doStuff(pickle.load(f))

bigDic ={}


def doStuff(row):
    #get live rows
    row = [cell for cell in row if cell!=[]]
    matches_ofa_row = [matches for matches, a, b in row]
    for cell in matches_ofa_row:
        doCellStuff(cell)


def doCellStuff(list_of_matches):
    print([[convertTuplets(match) for match in matches] for matches in list_of_matches])
    list_untupled_matched=[[convertTuplets(match) for match in matches] for matches in list_of_matches]
    #for some reason the sum function doesn't work on the above 
    match_list_cleaned = []
    for e in list_untupled_matched:
        match_list_cleaned+=e
    #order strings smallest to largest
    match_list_cleaned.sort(key=len)
    #put them in the hash
    if match_list_cleaned==[]:
        return 1
    main_match = match_list_cleaned[-1]
    if main_match in bigDic.keys():
        bigDic[main_match][0] += 1
        bigDic[main_match][1] += 1
    else:
        bigDic[main_match] = [1,1]
    for match in match_list_cleaned[:-1]:
        if match in bigDic.keys():
            bigDic[match][0] += 1
        else:
            bigDic[match] = [1,0]

#for i in range(len(list_untupled_matched)):
#    for n in range(i+1,len(list_untupled_matched)):
#        if list_untupled_matched[n].find(list_untupled_matched[i])!=-1:
#            yield (1,0)
#    yield (1,1)
