# read a file
# print value to terminal/console

from partb import sayposition
# f = open("day1-notaquitlisp\inputa.txt")
# data=f.read()
# f.close()
with open("day1-notaquitlisp\inputb.txt") as f:
    data = f.read()
    print(sayposition(data))
