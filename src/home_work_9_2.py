''''''
my_fanc = lambda ** kwargs: {key * 2: value for key, value in kwargs.items()}
print(my_fanc(abc = 5 , abcd= 5 , abcde = 5))



