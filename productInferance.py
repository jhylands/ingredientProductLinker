from X import match
import pickle

def save(acc,index):
    with open('/data/%d.pkl'%index,'wb') as f:
        pickle.dump(acc,f)

with open('/data/products_names_sort.pkl','rb') as f:
    p = pickle.load(f)

for i in range(0,len(p)):
    acc = [[] for a in range(i+1,len(p))]
    print(i)
    for n in range(i+1,min(len(p),i+5000)):                    
            acc[n] = [match(p[i][0],p[n][0]),p[i][1],p[n][1]]
    print('saving')
    save(acc,i)
    print('saved')
