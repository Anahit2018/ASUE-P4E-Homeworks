def prime_number(n):

    '''This function detects prime numbers from 0 to a given number.'''

    for integer in range(2,n+1): #modulus returns factors of 3,5,7 (ex. 9, 25, 49) as prime numbers. Manually ordered to return primes 3,5,7.. 
        if n==2:
            return True
        elif n==3:
            return True
        elif n==5:
            return True
        elif n==7:
            return True

        elif (n%integer==0): 
            return False

        elif (n%3==0): # ...but exclude numbers that can be devided by them. Keep looking for more laconic solution though
            return False
        elif (n%5==0):
            return False
        elif (n%7==0):
            return False

        else:
            return True

n=int(input("Input an integer between 1 and 100: "))
for x in range(1, n+1):
      if prime_number(x):
        print(x, end=' ')
print('\n')
