
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list = text.split(" ")

for i in range(len(list)):
    print(list[i])
    tmp = list[i].replace(",", "")
    list[i] = len(tmp)

print(list)