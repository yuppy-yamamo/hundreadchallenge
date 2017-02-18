# Question16.py [filename] [n]
import sys


def split_file(filename, num):
    file = open(filename)
    lines = file.readlines()
    line_length = len(lines)

    division_num = line_length / num
    surplus_num = line_length % num

    num_list = []
    for i in range(num):
        num_list.append(division_num)
    for i in range(surplus_num):
        num_list[i] += 1

    line_pointer = 0

    for i in range(len(num_list)):
        data = ""
        for j in range(int(num_list[i])):
            data += lines[line_pointer]
            line_pointer += 1
        name = "data%s.txt" % str(i + 1)
        file = open(name, "w")
        file.write(data)

if __name__ == "__main__":
    args = sys.argv
    split_file(args[1], int(args[2]))
