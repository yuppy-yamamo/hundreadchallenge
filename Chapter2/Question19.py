# -*- coding: utf-8 -*-
# Question19.py [filename]
import sys


def sort_emergence(filename):
    file = open(filename, "r")
    lines = file.readlines()

    dict = {}
    ans = []
    for i in range(len(lines)):
        tmp = lines[i].split("\t")
        lines[i] = tmp
        key = tmp[0]
        if key in dict:
            value = dict[key]
            value += 1
            dict[key] = value
        else:
            dict.update({key: 1})

    for k, v in sorted(dict.items(), key=lambda x: x[1]):
        tmp = [k ,v]
        ans.append(tmp)

    list_length = len(ans)

    for i in range(list_length):
        data = ans[list_length - i - 1][0] + " " + str(ans[list_length - i - 1][1])
        print(data)


if __name__ == "__main__":
    args = sys.argv
    sort_emergence(args[1])