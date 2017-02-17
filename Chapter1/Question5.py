
def bigram_search(obj):
    ans = []
    if isinstance(obj, list):
        # 与えられた物がリストの場合
        for i in range(len(obj)):
            ans.append(bigram_extraction(obj[i]))

    else:
        ans = bigram_extraction(obj)

    return ans


def bigram_extraction(str):
    li = []

    for i in range(len(str) - 1):
        tmp = str[i] + str[i + 1]
        li.append(tmp)

    return li


if __name__ == "__main__":
    str = "アイウエオ"
    li = ["カキクケコ", "サシスセソ"]
    str_list = bigram_search(str)
    print(str_list)
    li_list = bigram_search(li)
    print(li_list)