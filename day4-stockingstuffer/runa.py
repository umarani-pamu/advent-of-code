# read a file
# print value to terminal/console

from parta import find_adventcoin
with open("/home/uma/prime/gits/advent-of-code-2015/day4-stockingstuffer/inputa.txt") as f:
    data = f.read()
    print(find_adventcoin(data))

