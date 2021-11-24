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
    # print('called setSolutionAttempt function....::val', value)
    global solutionAttempt
    solutionAttempt = value

def calcDest1(src, dest, attempt):
    if attempt == 3:
        return False

    attempt += 1
    # print('calcDest1::src:dest:attempt', src, dest, attempt)
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
        return True
    else:
        [ setSolutionAttempt(attempt) for x in possibleDestinations if calcDest1(x, dest, attempt) ]
        return False

def calcDest2(src, dest, attempt):
    attempt += 1
    print('calcDest2::src:dest:attempt', src, dest, attempt)
    # print('attempt (in b)', attempt)

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

    if(not dest in possibleDestinations):
        if attempt == 3:
            return False

        # [print(x) for x in possibleDestinations]
        [calcDest1(x, dest, attempt) for x in possibleDestinations]
        return False
    else:
        print('YIKES, WE GOT ITTTTTTTTTTTTTTTTTTTTTTT.. at attempt number:', attempt)        
        return attempt

def calcDest3(src, dest, attempt):
    attempt += 1
    print('calcDest3::src:dest:attempt', src, dest, attempt)
    # print('attempt (in c)', attempt)

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

    if(not dest in possibleDestinations):
        # [print(x) for x in possibleDestinations]
        # [calcDest(x, dest, attempt) for x in possibleDestinations dest in possibleDestinations]
        return False
    else:
        print('YIKES, WE GOT ITTTTTTTTTTTTTTTTTTTTTTT.. at attempt number:', attempt)        
        return attempt

solutionAttempt = 0

def solution(src,dest):
    attempt = 0

    calcDest1(src, dest, attempt)
    # print('solutionAttempt', solutionAttempt)
    return solutionAttempt

print('MY SOLUTION IS:', solution(0, 1))
# solution(45)
# solution(1)
# solution(2)
# solution(63)
# solution(31)
# solution(17)

