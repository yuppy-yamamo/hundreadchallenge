import random


def change_number(word_list):
    ans = ""
    for i in range(len(word_list)):
        if len(word_list[i]) < 4:
            word = word_list[i]
            pass
        else:
            mid = word_list[i][1:-1]
            shuffle = random.sample(mid, len(mid))
            tmp = "".join(shuffle)
            word = word_list[i][0] + tmp + word_list[i][len(word_list[i]) - 1]
        ans += word + " "
    return ans


if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    word_list = text.split(" ")
    print(text)
    print(change_number(word_list))