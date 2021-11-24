
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
    global solutionAttempt
    if(solutionAttempt is None):
        solutionAttempt = value
        # print('initially solutionAttempt as:', value)
    if(value < solutionAttempt):
        solutionAttempt = value
        # print('new solutionAttempt as:', value)

def calcDest(src, dest, attempt):
    if attempt == 6:
        global count
        count += 1
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
        setSolutionAttempt(attempt)
        return True
    else:
        [ setSolutionAttempt(attempt + 1) for x in possibleDestinations if calcDest(x, dest, attempt) ]
        return False

solutionAttempt = None
count = 1

def solution(src,dest):
    if(src == dest): return 0
    attempt = 0
    calcDest(src, dest, attempt)
    return solutionAttempt
    