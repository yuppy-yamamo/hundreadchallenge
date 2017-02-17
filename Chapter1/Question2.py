
text1 = "パトカー"
text2 = "タクシー"
ans = ""

length1 = len(text1)
length2 = len(text2)

if length1 == length2:
    for i in range(length1):
        ans += text1[i]
        ans += text2[i]

print(ans)