from itertools import chain,combinations
def X(A,B):
    assert(len(B)>=len(A))
    if len(B)==0 or len(A)==0:
        return []
    if len(A)==1:
        return [ [A[0]] for b in B if b==A[0] ]
    if len(A)==len(B):
        if A==B:
            return A
            #return [[a] for a,b in zip(A,B)]
        else:
            return []

    acc=[]
    for n in range(0,len(B)-len(A)):
        if A[0]==B[n]:
            try:
                acc += map( lambda x:[ A[0] ] + x , X(A[1:],B[n+1:]) )
            except:
                print(X(A[1:],B[n+1:]))
                print(A)
                print(B)
                print(1/0)
    return acc

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def filtELst(array):
    return [a for a in array if a!=[]]

def match(A):
    PA = powerset(A)
    return (lambda B : 0 if A==B else filtELst([X(sub,B) for sub in PA]))
#    a = product_a['title'].split(' ')
#    b = product_b['title'].split(' ')
#make the assumption that they are ordered
#    if len(A)>len(B):
#        c=A
#        A=B
#        B=c
#    if A==B:
#        return [] #save on computation don't bother if they are the same
    for sub in PA:                        
        z = X(sub,b)                  
        if z!=[]:                     
            if len(z[0])>len(acc):
                acc = z[0] 
    return acc
