# Question17.py [filename]
import sys


def generate_uniq_list(filename):
    file = open(filename, "r",)
    lines = file.readlines()
    word_list = []
    for i in range(len(lines)):
        tmp = lines[i].split("\t")
        if tmp[0] not in word_list:
            word_list.append(tmp[0])

    for i in word_list:
        print(i)


if __name__ == "__main__":
    args = sys.argv
    generate_uniq_list(args[1])