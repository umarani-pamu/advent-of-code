# read a file
# print value to terminal/console

from partb import count_new_nicestring
with open("/home/uma/prime/gits/advent-of-code-2015/day5-internelves/inputb.txt") as f:
    data = f.readlines()
    print(count_new_nicestring(data))

