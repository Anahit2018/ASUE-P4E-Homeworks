#SOLUTION APPROACH
#1. Form a range between 0 and inputed number
#2. Take each number from range and divide by its predecessors.If divisable by any (num%i==0) not a prime, take it out. Prime divisible to only 1(which we exclude in function) and itself.
#3. Print whatever stayed (primes)

random_num = int(input("Input an integer: "))

print("Prime numbers between 0 and", random_num,"are:")

for num in range(0, random_num+ 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num, end=' ')
print('\n')
