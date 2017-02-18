
def union_search(union_set1, union_set2):
    # 和集合を求めるメソッド
    union = []
    union.extend(union_set1)
    for i in range(len(union_set2)):
        if union_set2[i] not in union:
            union.append(union_set2[i])
    return union


def intersection_search(inter_set1, inter_set2):
    # 積集合を求めるメソッド
    intersection = []
    for i in range(len(inter_set1)):
        for j in range(len(inter_set2)):
            if inter_set1[i] == inter_set2[j]:
                intersection.append(inter_set1[i])
    return intersection


def difference_search(diff_set1, diff_set2):
    # set1 - set2 の差集合を求めるメソッド
    difference = []
    difference.extend(diff_set1)
    for i in range(len(diff_set2)):
        if diff_set2[i] in difference:
            difference.remove(diff_set2[i])
    return difference


def generate_bigram_set(str):
    # 集合の生成　重複は除く
    bigram_set = []
    for i in range(len(str) - 1):
        tmp = str[i] + str[i + 1]
        if tmp not in bigram_set:
            bigram_set.append(tmp)
    return bigram_set


if __name__ == "__main__":
    text1 = "paraparaparadise"
    text2 = "paragraph"

    set_X = generate_bigram_set(text1)
    set_Y = generate_bigram_set(text2)
    print(set_X)
    print(set_Y)

    print("和集合")
    print(union_search(set_X, set_Y))
    print("積集合")
    print(intersection_search(set_X, set_Y))
    print("X-Y差集合")
    print(difference_search(set_X, set_Y))
    print("Y-X差集合")
    print(difference_search(set_Y, set_X))
