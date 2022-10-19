#string compression
#aaaabbbcddeee->a4b3c1d2e3
def string_compress(word):
    new_string = ""
    count = 0
    for i in range(len(word)):
        for j in range(len(word+1)):
            if word[i] == word[j]:
                


if __name__ == "__main__":
    string_compress('aaabbbcdddeeeff')