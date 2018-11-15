def check_if_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for integer in range(2, n+1):
        if n % integer==0:
            return False
        return True

def prime_finder(n):
    primes_list=[]
    for a in range(2,n+1): 
        if check_if_prime(a):
            primes_list.append(a)
    return primes_list

n=int(input("Input an integer larger than one: "))
primes_list=prime_finder(n)
for x in range(len(primes_list)):
    print(primes_list[x], end=' ')
print('\n')
