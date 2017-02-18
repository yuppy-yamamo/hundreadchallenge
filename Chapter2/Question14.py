# Question14.py [filename] [n]
import sys

args = sys.argv

filename = args[1]
n = int(args[2])

file = open(filename)
lines = file.readlines()

for i in range(n):
    print(lines[i].replace("\n", ""))
