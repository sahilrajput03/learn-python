# Notes:
# tl, tr, rt ... respectively means top-left, top-right, right-top...

def tl(src):
    if(src % 8 > 0 and src > 16 ):
        return src - 17

def tr(src):
    if( src % 8 < 7 and src > 15):
        return src - 15

def rt(src):
    if(src > 7 and src % 8 < 6):
        return src - 6

def rb(src):
    if(src < 54 and src % 8 < 6):
        return src + 10

def br(src):
    if(src < 47 and src % 8 < 7):
        return src + 17

def bl(src):
    if(src < 48 and src % 8 > 0):
        return src + 15

def lt(src):
    if(src % 8 > 1 and src > 9):
        return src - 10

def lb(src):
    if(src % 8 > 1 and src < 56):
        return src + 6

def calcDest(src):
    # print('calcDest:src', src)

    possibleDestinations = []

    tld = tl(src)
    if(not tld is None):
        possibleDestinations.append(tld)

    trd = tr(src)
    if(not trd is None):
        possibleDestinations.append(trd)

    rtd = rt(src)
    if(not rtd is None):
        possibleDestinations.append(rtd)

    rbd = rb(src)
    if(not rbd is None):
        possibleDestinations.append(rbd)

    brd = br(src)
    if(not brd is None):
        possibleDestinations.append(brd)

    bld = bl(src)
    if(not bld is None):
        possibleDestinations.append(bld)

    lbd = lb(src)
    if(not lbd is None):
        possibleDestinations.append(lbd)

    ltd = lt(src)
    if(not ltd is None):
        possibleDestinations.append(ltd)

    return possibleDestinations

def solution(src,dest):
    node = None
    if( src == dest): return 0

    # print('We need shortest path from ', src, 'to ', dest)
    attempt = 0
    queue = []
    queue.append(src)
    attempt += 1
    found = False
    popped = []
    while(queue):
        node = queue.pop(0)
        popped.append(node)
        possibilities = calcDest(node)
        
        for el in possibilities:
            if(el == dest):
                found = True
                break
                
        if(found == True): break
        
        attempt += 1
        queue.extend(possibilities)

    attempt

    return attempt

s1 = solution(0, 1)
e1 = 3
print('0 -> 1', "PASSED" if s1 == e1  else  "_failed_  got " + str(s1) + ", expected " + str(e1)) # solution: 3 from ggl.

s2 = solution(19, 36)
e2 = 1
print('19 -> 36', "PASSED" if s2 == e2  else  "_failed_  got " + str(s2) + ", expected " + str(e2)) # solution: 1 from ggl.

# s3 = solution(19, 19)
# e3 = 0
# print('19 -> 19', "PASSED" if s3 == e3  else  "_failed_  got " + str(s3) + ", expected " + str(e3)) # solution: 0 from ggl.

# s4 = solution(34, 2)
# e4 = 2
# print('34 -> 2', "PASSED" if s4 == e4  else  "_failed_  got " + str(s4) + ", expected " + str(e4)) # solution: 2 from myself.

# s5 = solution(34, 38)
# e5 = 2
# print('34 -> 2', "PASSED" if s5 == e5  else  "_failed_  got " + str(s5) + ", expected " + str(e5)) # solution: 2 from geeksforgeeks.


# learnig not operator with null check (add it to notes):
# foo = None
# print(not foo is None)