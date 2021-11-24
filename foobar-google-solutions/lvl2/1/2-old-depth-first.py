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

def setSolutionAttempt(value):
    print('setSolutionAttempt called with value:', value)
    global solutionAttempt
    if(solutionAttempt is None):
        solutionAttempt = value
        # print('initially solutionAttempt as:', value)
    if(value < solutionAttempt):
        solutionAttempt = value
        # print('new solutionAttempt as:', value)

def calcDest(src, dest, attempt):
    print('calcDest:src:attempt', src, attempt)

    # global solutionAttempt
    # if(not solutionAttempt is None and solutionAttempt <= attempt):
    #     print('hel')
    #     return False

    if attempt == 4:
        global count
        count += 1
        print(count, 'hel')
        return False

    attempt += 1
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

    if(dest in possibleDestinations):
        # print('got it....')
        setSolutionAttempt(attempt)
        return True
    else:
        [ setSolutionAttempt(attempt + 1) for x in possibleDestinations if calcDest(x, dest, attempt) ]
        return False

solutionAttempt = None
count = 1

def solution(src,dest):
    if(src == dest): return 0
    print('We need shortest path from ', src, 'to ', dest)
    attempt = 0

    calcDest(src, dest, attempt)
    # print('solutionAttempt', solutionAttempt)
    return solutionAttempt

# print('MY SOLUTION IS:', solution(0, 1))
print('MY SOLUTION IS:', solution(19, 36))
# print('MY SOLUTION IS:', solution(45, 45))

# solution(1)
# solution(2)
# solution(63)
# solution(31)
# solution(17)

# learnig not operator with null check (add it to notes):
# foo = None
# print(not foo is None)