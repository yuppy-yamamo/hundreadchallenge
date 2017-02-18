
def cipher(text):
    ans = ""
    for i in text:
        if i.islower():
            ans += chr(216 - ord(i))
        else:
            ans += i
    return ans


if __name__ == "__main__":
    text = "Attached is a report on the new product."
    str = cipher(text)
    print(str)
    str = cipher(str)
    print(str)
