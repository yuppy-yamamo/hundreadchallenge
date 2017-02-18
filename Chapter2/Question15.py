# Question15.py [filename] [n]
import sys

args = sys.argv

filename = args[1]
n = int(args[2])

file = open(filename)
lines = file.readlines()

data = ""
list_length = len(lines)

for i in range(n):
    line = int(list_length - i - 1)
    data = lines[line] + data
print(data)