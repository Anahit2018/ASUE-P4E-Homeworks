random_num = int(input("Input an integer: "))
random_list = list(range(0, random_num+1))
#print(random_list)

def find_prime(random_list):
    for num in random_list:
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
       else:
           print(num)
