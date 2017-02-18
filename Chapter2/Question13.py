
text1 = open("col1.txt")
text2 = open("col2.txt")

lines1 = text1.readlines()
lines2 = text2.readlines()
data = ""

for i in range(len(lines1)):
    tmp = lines1[i].replace("\n", "") + "\t" + lines2[i].replace("\n", "")
    print(tmp)
    data += tmp + "\n"

file = open("13.txt", "w")
file.write(data)