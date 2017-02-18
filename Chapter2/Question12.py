
text = open("hightemp.txt")
lines = text.readlines()

tab1 = ""
tab2 = ""

for i in lines:
    tmp = i.split("\t")
    tab1 += tmp[0] + "\n"
    tab2 += tmp[1] + "\n"

file1 = open("col1.txt", "w")
file1.write(tab1)
file2 = open("col2.txt", "w")
file2.write(tab2)