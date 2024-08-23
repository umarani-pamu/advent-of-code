# read a file
# print value to terminal/console

from parta import count_nicestring
with open("/home/uma/prime/gits/advent-of-code-2015/day5-internelves/inputa.txt") as f:
    data = f.readlines()
    print(count_nicestring(data))

