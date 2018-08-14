import re
class wordType():
    def __init__(self):
        word_capture_re = re.compile(r"^(\D*)\d?\s\s(—?[a-z]+\.)")
        with open('words.txt' ,'r') as f:
            dictionary = f.read().split('\n')
        matched_dic = [word_capture_re.search(a) for a in dictionary]
        d = {}
        matched_dic = [a for a in matched_dic if a!=None]
        for g in matched_dic:
            try:
                d[g.group(2)].append(g.group(1))
            except (AttributeError,KeyError) as e:
                d[g.group(2)] = [g.group(1)]
            
        inv_d = {i.strip().lower():j for i,j in sum([[(v_,k) for v_ in v] for k, v in d.items()],[])}

        self.dictionary = inv_d

    def __call__(self,word):
        #need to check the word here
        return self.dictionary[word]
