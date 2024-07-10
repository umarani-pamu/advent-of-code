# read a file
# print value to terminal/console

from parta import whatfloor
# f = open("day1-notaquitlisp\inputa.txt")
# data=f.read()
# f.close()
with open("day1-notaquitlisp\inputa.txt") as f:
    data = f.read()
    print(whatfloor(data))
