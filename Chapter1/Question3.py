
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

li = text.split(" ")

for i in range(len(li)):
    print(li[i])
    tmp = li[i].replace(",", "")
    li[i] = len(tmp)

print(li)