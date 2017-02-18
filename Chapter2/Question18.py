# -*- coding: utf-8 -*-
# Question18.py [filename]
import sys


def generate_sort_list(filename):
    file = open(filename, "r")
    lines = file.readlines()

    dict = {}
    ans = []
    for i in range(len(lines)):
        tmp = lines[i].split("\t")
        lines[i] = tmp
        data = ""
        for j in range(len(tmp)):
            data += tmp[j] + "\t"

    for i in range(len(lines)):
        dict.update({str(i): float(lines[i][2])})

    for k, v in sorted(dict.items(), key=lambda x:x[1]):
        ans.append(k)

    line_length = len(ans)
    for i in range(line_length):
        num = int(ans[line_length - i - 1])
        tmp = lines[num]
        data = ""
        for j in range(len(tmp)):
            data += tmp[j].replace("\n", "") + "\t"
        print(data)

if __name__ == "__main__":
    args = sys.argv
    generate_sort_list(args[1])