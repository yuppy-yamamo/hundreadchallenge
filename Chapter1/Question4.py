
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

li = text.split(" ")

un = [1,5,6,7,8,9,15,16,19]

for i in range(len(li)):
    pointer = i+1
    if pointer in un:
        li[i] = li[i][0:1]
    else:
        print(li[i])
        li[i] = li[i][0:2]

print(li)