#Given two strings, write a method to decide if one is a permutation of the other
#idea is use a hashtable
#other idea is to organize both strings and see if they are equal


def check_perm2(w1, w2):
    #O(nlgn)
    nw1 = sorted(w1)
    nw2 = sorted(w2)
    if nw1 == nw2:
        print("Yes they are permutations.")
    else:
        print("No")



if __name__ == "__main__":
    check_perm2('mchado', 'odach')