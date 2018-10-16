import itertools

f = open("permA.txt", "w")
my_list = ['a','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
s = ""
from itertools import permutations
for i in permutations(my_list,5):
    if 'a' in i:
        f.write(s.join(i)+ '\n')
