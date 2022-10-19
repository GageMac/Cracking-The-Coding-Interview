#URLify
#idea, go through each index and check for a space
#if you see a space, replace it with %20
#python makes this easy with '.replace().
#.replace() expects 2 arguments, first is the char to replace, second is what to replace it with.
def urlify(word):
    word = word.replace(' ', '%20')
    print(word)

if __name__ == "__main__":
    urlify('mr john smith')