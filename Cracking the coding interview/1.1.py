def is_unique(word):
    l = list(word)
    if(len(set(l)) == len(word)):
        print('All letters are unique.')
    else:
        print('Not all letters are unique.')


if __name__ == "__main__":
    is_unique('mchado')

