



def list(l):

    l1 = []

    for word in l:
        if word == word[::-1]:
            l1.append(word)
    print(l1)


l = ['mother', 'father', 'dad']



list(l)