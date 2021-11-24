import time, datetime
# a,b = 1,2
# print(a,b)

# x = '1**10'
# print('x.isnumeric()', not x.isnumeric())

# print(int(5/2))
#  5/2 -> 2.5
# int(5/2) -> 2 (i.e., it rounds off)

# Python automatically maanges large sized numbers, yikes!! No need to use biginterger of float or anything else.
# a = 123456789012345678901234567890123456789012345678901234567890
# print(a) # 123456789012345678901234567890123456789012345678901234567890
# a+=1
# print(a) # 123456789012345678901234567890123456789012345678901234567891


# test
# while True:
#     print('hell')
#     if 5 > 2:
#         break


#  benchmarking in pytohn using time library.
print('hel')
start = time.perf_counter() # src: https://stackoverflow.com/a/58569410
# time.sleep(3) #LEARN PYTHON sleep for 3 seconds in python

i = 0
while i < 1_000_000:
    # print('hel') # .08s without print, and 3.72s with uncommented.
    i = i + 1



end = time.perf_counter()
print(end - start)
