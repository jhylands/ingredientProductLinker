from X1 import match
import pickle
import time
def save(acc,index):
    with open('data/%d.pkl'%index,'wb') as f:
        pickle.dump(acc,f)

with open('productNumberLists.pkl','rb') as f:
    p = pickle.load(f)

for i in range(0,len(p)):
    s = time.time()
    acc = [[] for a in range(i+1,len(p))]
    print(i)
    for n in range(i+1,len(p)):                    
            acc[n-i-1] = match(p[i],p[n])
    print('time:%d'%(time.time()-s))
    print('saving')
    save(acc,i)
    print('saved')
