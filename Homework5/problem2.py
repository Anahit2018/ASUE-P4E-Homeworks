
string = input('Enter your word: ')
import itertools

found = False
char_set = set(string) # find unique letters

d_dict = {}
for c in char_set:
    d_dict[c] = string.count(c) #  count letters

odd_l = [e for e in d_dict.values() if e%2 == 1] 
if len(odd_l) >1:
    pass
    
else:
    found = True
    
if not found:
    print("Impossible")
else:
    def permutation(string):
      for i in range(len(string)+1):
          perms=list(itertools.permutations(string))
          for i in perms:
            j=(''.join(i))
            j=j.casefold()
            k=reversed(j)
            if list(j)==list(k):
                print(j)
    print(permutation(string))


