n = int(input("Input a natural number to get its factorial: "))
cache = {}

def factorial(n, cache):
    '''Returns the factorial of a number.'''
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    else:
        ans = n*factorial(n-1, cache)
        cache[n] = ans
        return ans

print(factorial(n, cache))

while n is not "exit":
    n = int(input("Input another number or type 'exit' to leave: "))
    print(factorial(n, cache))

    if n == str(n) and n == "exit":
        # tried option but cant exit w/o error
        break
