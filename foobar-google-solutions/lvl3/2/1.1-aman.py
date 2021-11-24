import time
def rescur(l):
    m = max(l)  
    l.remove(m); 
    factor = [x for x in l if m%x==0]
    return factor;

def fl(n):
    for i in range(1,n+1):
        fact = fact * i
    return fact

def solution(l):
    no_of_triples = 0;
    for x in l:
        fact = rescur(l)
        if len(fact) > 1:
            no_of_triples += fl(len(fact)/2/fl(len(fact-2)
    return no_of_triples

