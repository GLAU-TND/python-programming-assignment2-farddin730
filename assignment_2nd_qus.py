from itertools import permutations 
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
       
        lst.append("".join(map(str,i)))  
    return max(lst) 
ls=[]
n=int(input('enter the no of element you have to enter'))
for i in range(0,n) :
    ls.append(int(input()))
print(largest(ls))
