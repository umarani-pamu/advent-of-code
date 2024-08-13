# read a file
# print value to terminal/console

from parta import countuniquehouses
with open("/home/uma/prime/gits/advent-of-code-2015/day3-housesinavaccum/inputa.txt") as f:
    data = f.read()
    print(countuniquehouses(data))

