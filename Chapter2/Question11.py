import sys

text = open("hightemp.txt")
lines = text.readlines()
print(lines)

for i in lines:
    line = i.replace("\t", " ")
    sys.stdout.write(line)
    print(line)