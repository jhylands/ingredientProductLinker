from itertools import chain,combinations
def X(A,B):
    assert(len(B)>=len(A))
    if len(B)==0 or len(A)==0:
        return []
    if len(A)==1:
        return [[(A[0],b)] for b in B if b==A[0]]
    if len(A)==len(B):
        if A==B:
            return [(a,b) for a,b in zip(A,B)]
        else:
            return []

    acc=[]
    for n in range(0,len(B)-len(A)):
        if A[0]==B[n]:
            acc += map( lambda x:[(A[0],B[n])]+x , X(A[1:],B[n+1:]) )
    return acc

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def match(A,B):
#    a = product_a['title'].split(' ')
#    b = product_b['title'].split(' ')
    if len(A)>len(B):
        c=A
        A=B
        B=c
    if A==B:
        return [] #save on computation don't bother if they are the same
    acc=[]
    PA = powerset(A)
    return [X(sub,B) for sub in PA]
    for sub in PA:                        
        z = X(sub,b)                  
        if z!=[]:                     
            if len(z[0])>len(acc):
                acc = z[0] 
    return acc
