from X2 import match as matchGenerator
import pickle
import time
def save(acc,index):
    with open('data/%d.pkl'%index,'wb') as f:
        pickle.dump(acc,f)

with open('OrderedproductNumberLists.pkl','rb') as f:
    p = pickle.load(f)

for i in range(0,len(p)):
    s = time.time()
    acc = [[] for a in range(i+1,len(p))]
    print(i)
    match = matchGenerator(p[i])
    for n in range(i+1,len(p)):                    
            acc[n-i-1] = match(p[n])
    print('time:%f'%(time.time()-s))
    print('saving')
    save(acc,i)
    print('saved')
