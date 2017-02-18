
def bigram_search(obj):
    ans = []
    if isinstance(obj, list):
        # 与えられた物がリストの場合
        for i in range(len(obj)):
            ans.append(bigram_extraction(obj[i]))

    else:
        tmp = obj.replace(" ", "")
        ans = bigram_extraction(tmp)

    return ans


def bigram_extraction(str):
    li = []

    for i in range(len(str) - 1):
        tmp = str[i] + str[i + 1]
        li.append(tmp)

    return li


if __name__ == "__main__":
    text = "I am an NLPer"
    ans_list = bigram_search(text)
    print(ans_list)