# read a file
# print value to terminal/console

from parta import calculate_wrapping
with open("/home/uma/prime/gits/advent-of-code-2015/day2-therewouldbenomath/inputa.txt") as f:
    data = f.readlines()

total_wrapping=0
for line in data:
    dimensions = line.strip().split('x')
    length, width, height = map(int, dimensions)
    wrapping = calculate_wrapping(length, width, height)
    total_wrapping += wrapping

print(total_wrapping)

