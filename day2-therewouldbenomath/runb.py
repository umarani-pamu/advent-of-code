# read a file
# print value to terminal/console

from partb import calculate_ribbon

with open("/home/uma/prime/gits/advent-of-code-2015/day2-therewouldbenomath/inputb.txt") as f:
    data = f.readlines()

total_wrapping=0
for line in data:
    dimensions = line.strip().split('x')
    length, width, height = map(int, dimensions)
    wrapping = calculate_ribbon(length, width, height)
    total_wrapping += wrapping

print(total_wrapping)

