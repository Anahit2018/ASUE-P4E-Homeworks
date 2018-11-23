x = float(input("Pick initial value for x: "))
n = int(input("Pick number of iterations: "))

count = 0
eps = 0.00001


def f(x):
    return round((0.05*(x**4)+0.1*(x**3)+0.5*(x**2)+10*x+5), 2)


def f_d1(x):
    return 0.2*x**3+0.3*x**2+x+10


def f_d2(x):
    return 0.6*x**2+0.6*x+1

while abs(f(x)) >= eps:
    if n != count:
        x = x - (f_d1(x))/(f_d2(x))
        x = round(x, 2)
        count += 1
    else:
        break

    print("Estimated value of minimum x after iteration",
          count, ":", (round(x, 2)))
print("\n")
print("Minimum x value:", x)
print("Minimum function value:", f(x))
